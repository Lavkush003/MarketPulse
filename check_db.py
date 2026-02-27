from app import app
from extensions import db
from models import User, Product

with app.app_context():
    try:
        user_count = User.query.count()
        product_count = Product.query.count()
        print(f"Users: {user_count}")
        print(f"Products: {product_count}")
    except Exception as e:
        print(f"Error: {e}")
