import os
from dotenv import load_dotenv
load_dotenv()
from flask import Flask, render_template, url_for, flash, redirect, request, abort
from flask_login import LoginManager, login_user, current_user, logout_user, login_required
from werkzeug.security import generate_password_hash, check_password_hash
from werkzeug.utils import secure_filename
from extensions import db
from flask_migrate import Migrate
from config import Config

app = Flask(__name__)
app.config.from_object(Config)

# Ensure upload directory exists
os.makedirs(app.config['UPLOAD_FOLDER'], exist_ok=True)

db.init_app(app)
# Initialize Flask-Migrate for handling migrations
migrate = Migrate(app, db)

# Import models and forms AFTER db.init_app to avoid registry issues
from models import User, Product, Cart, Order, OrderItem
from forms import RegistrationForm, LoginForm, ProductForm

login_manager = LoginManager(app)
login_manager.login_view = 'login'
login_manager.login_message_category = 'info'

@login_manager.user_loader
def load_user(user_id):
    return User.query.get(int(user_id))

# --- Routes ---

@app.route('/')
@app.route('/home')
def home():
    category = request.args.get('category')
    subcategory = request.args.get('subcategory')
    
    query = Product.query
    if category:
        query = query.filter_by(category=category)
    if subcategory:
        query = query.filter_by(subcategory=subcategory)
        
    products = query.all()
    return render_template('index.html', products=products)

@app.route('/product/<int:product_id>')
def product_detail(product_id):
    product = Product.query.get_or_404(product_id)
    return render_template('product_detail.html', product=product)

@app.route('/register', methods=['GET', 'POST'])
def register():
    if current_user.is_authenticated:
        return redirect(url_for('home'))
    form = RegistrationForm()
    if form.validate_on_submit():
        hashed_password = generate_password_hash(form.password.data)
        user = User(username=form.username.data, email=form.email.data, password=hashed_password)
        db.session.add(user)
        db.session.commit()
        flash('Account created! Please log in to continue.', 'success')
        return redirect(url_for('login'))
    return render_template('register.html', title='Register', form=form)

@app.route('/login', methods=['GET', 'POST'])
def login():
    if current_user.is_authenticated:
        return redirect(url_for('home'))
    form = LoginForm()
    if form.validate_on_submit():
        user = User.query.filter_by(email=form.email.data).first()
        if user and check_password_hash(user.password, form.password.data):
            login_user(user)
            next_page = request.args.get('next')
            return redirect(next_page) if next_page else redirect(url_for('home'))
        else:
            flash('Login Unsuccessful. Please check email and password', 'danger')
    return render_template('login.html', title='Login', form=form)

@app.route('/logout')
def logout():
    logout_user()
    return redirect(url_for('home'))

# --- Cart System ---

@app.route('/cart')
@login_required
def cart():
    items = Cart.query.filter_by(user_id=current_user.id).all()
    total = sum(item.product.price * item.quantity for item in items)
    return render_template('cart.html', items=items, total=total)

@app.route('/add_to_cart/<int:product_id>')
@login_required
def add_to_cart(product_id):
    product = Product.query.get_or_404(product_id)
    cart_item = Cart.query.filter_by(user_id=current_user.id, product_id=product_id).first()
    if cart_item:
        cart_item.quantity += 1
    else:
        cart_item = Cart(user_id=current_user.id, product_id=product_id)
        db.session.add(cart_item)
    db.session.commit()
    flash('Product added to cart!', 'success')
    return redirect(url_for('cart'))

@app.route('/remove_from_cart/<int:cart_id>')
@login_required
def remove_from_cart(cart_id):
    item = Cart.query.get_or_404(cart_id)
    if item.user_id != current_user.id:
        abort(403)
    db.session.delete(item)
    db.session.commit()
    flash('Item removed from cart.', 'info')
    return redirect(url_for('cart'))

@app.route('/update_cart/<int:cart_id>/<action>')
@login_required
def update_cart(cart_id, action):
    cart_item = Cart.query.get_or_404(cart_id)
    if cart_item.user_id != current_user.id:
        abort(403)
    
    if action == 'increase':
        if cart_item.product.stock > cart_item.quantity:
            cart_item.quantity += 1
            db.session.commit()
        else:
            flash(f'Sorry, only {cart_item.product.stock} items in stock.', 'warning')
    elif action == 'decrease':
        if cart_item.quantity > 1:
            cart_item.quantity -= 1
            db.session.commit()
        else:
            db.session.delete(cart_item)
            db.session.commit()
            flash('Item removed from cart.', 'info')
    
    return redirect(url_for('cart'))

# --- Checkout & Orders ---

@app.route('/checkout', methods=['POST'])
@login_required
def checkout():
    cart_items = Cart.query.filter_by(user_id=current_user.id).all()
    if not cart_items:
        flash('Your cart is empty!', 'warning')
        return redirect(url_for('home'))
    
    total_price = sum(item.product.price * item.quantity for item in cart_items)
    
    # Create Order
    order = Order(user_id=current_user.id, total_price=total_price)
    db.session.add(order)
    
    # Transfer items to OrderItem and update stock
    for item in cart_items:
        if item.product.stock < item.quantity:
            flash(f'Sorry, {item.product.name} is out of stock!', 'danger')
            return redirect(url_for('cart'))
        
        order_item = OrderItem(
            order=order,
            product_id=item.product_id,
            quantity=item.quantity,
            price=item.product.price
        )
        item.product.stock -= item.quantity
        db.session.add(order_item)
        db.session.delete(item) # Clear cart item
    
    db.session.commit()
    flash('Order placed successfully! Thank you for your purchase.', 'success')
    return redirect(url_for('orders'))

@app.route('/orders')
@login_required
def orders():
    user_orders = Order.query.filter_by(user_id=current_user.id).order_by(Order.created_at.desc()).all()
    return render_template('orders.html', orders=user_orders)

@app.route('/search')
def search():
    query = request.args.get('q')
    if query:
        products = Product.query.filter(Product.name.contains(query) | Product.description.contains(query)).all()
    else:
        products = []
    return render_template('index.html', products=products, title=f"Search: {query}")

@app.route('/profile')
@login_required
def profile():
    return render_template('profile.html', title='My Profile')

@app.route('/contact', methods=['GET', 'POST'])
def contact():
    if request.method == 'POST':
        flash('Thank you for your message! Our team will get back to you soon.', 'success')
        return redirect(url_for('home'))
    return render_template('contact.html', title='Contact Us')

# --- Admin CRUD ---

@app.route('/admin/dashboard')
@login_required
def admin_dashboard():
    if not current_user.is_admin:
        abort(403)
    products = Product.query.all()
    return render_template('admin/dashboard.html', products=products)

@app.route('/admin/product/new', methods=['GET', 'POST'])
@login_required
def add_product():
    if not current_user.is_admin:
        abort(403)
    form = ProductForm()
    if form.validate_on_submit():
        image_file = 'default.jpg'
        if form.image.data:
            filename = secure_filename(form.image.data.filename)
            form.image.data.save(os.path.join(app.config['UPLOAD_FOLDER'], filename))
            image_file = filename
        
        product = Product(
            name=form.name.data,
            description=form.description.data,
            price=form.price.data,
            stock=form.stock.data,
            category=form.category.data,
            subcategory=form.subcategory.data,
            image_file=image_file
        )
        db.session.add(product)
        db.session.commit()
        flash('Product has been added!', 'success')
        return redirect(url_for('admin_dashboard'))
    return render_template('admin/add_product.html', title='New Product', form=form)

@app.route('/admin/product/<int:product_id>/edit', methods=['GET', 'POST'])
@login_required
def edit_product(product_id):
    if not current_user.is_admin:
        abort(403)
    product = Product.query.get_or_404(product_id)
    form = ProductForm()
    if form.validate_on_submit():
        if form.image.data:
            filename = secure_filename(form.image.data.filename)
            form.image.data.save(os.path.join(app.config['UPLOAD_FOLDER'], filename))
            product.image_file = filename
        
        product.name = form.name.data
        product.description = form.description.data
        product.price = form.price.data
        product.stock = form.stock.data
        product.category = form.category.data
        product.subcategory = form.subcategory.data
        db.session.commit()
        flash('Product has been updated!', 'success')
        return redirect(url_for('admin_dashboard'))
    elif request.method == 'GET':
        form.name.data = product.name
        form.description.data = product.description
        form.price.data = product.price
        form.stock.data = product.stock
        form.category.data = product.category
        form.subcategory.data = product.subcategory
    return render_template('admin/edit_product.html', title='Edit Product', form=form, product=product)

@app.route('/admin/product/<int:product_id>/delete', methods=['POST'])
@login_required
def delete_product(product_id):
    if not current_user.is_admin:
        abort(403)
    product = Product.query.get_or_404(product_id)
    db.session.delete(product)
    db.session.commit()
    flash('Product has been deleted!', 'success')
    return redirect(url_for('admin_dashboard'))

if __name__ == '__main__':
    with app.app_context():
        # db.create_all()
        admin = User.query.filter_by(email='admin@market.com').first()
        if not admin:
            hashed_pw = generate_password_hash('admin123')
            admin = User(username='admin', email='admin@market.com', password=hashed_pw, is_admin=True)
            db.session.add(admin)
            db.session.commit()
    app.run(debug=True)
