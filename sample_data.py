from app import app
from models import Product, User

with app.app_context():
    products = Product.query.limit(5).all()
    print(f"Total Products: {Product.query.count()}")
    for p in products:
        print(f"- {p.name} ({p.category})")
    
    users = User.query.all()
    print(f"Total Users: {len(users)}")
    for u in users:
        print(f"- {u.username} ({u.email})")
