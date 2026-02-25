from app import app, db
from models import User, Product, Cart, Order, OrderItem

with app.app_context():
    print("Mapping models...")
    try:
        db.create_all()
        print("Success!")
    except Exception as e:
        print(f"Error: {e}")
        import traceback
        traceback.print_exc()
