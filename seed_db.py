from extensions import db
from models import Product, User
from app import app
from werkzeug.security import generate_password_hash

def seed_data():
    with app.app_context():
        # Clean start
        db.drop_all()
        db.create_all()

        # Create Admin
        admin = User(
            username='admin', 
            email='admin@market.com', 
            password=generate_password_hash('admin123'), 
            is_admin=True
        )
        db.session.add(admin)

        # Diverse Global Product Catalog (All Categories)
        products = [
            # --- TECH (ELECTRONICS) ---
            Product(
                name="Ultra-Slim Laptop Pro",
                description="High-performance 14-inch laptop with 16GB RAM and 512GB SSD. Perfect for professionals and students.",
                price=899.00, stock=10, category="Electronics", subcategory="Laptops",
                image_file="laptop.jpg"
            ),
            Product(
                name="iPhone 15 Pro Max",
                description="Ultimate flagship smartphone with titanium body, A17 Pro chip, and advanced camera system.",
                price=1199.00, stock=8, category="Electronics", subcategory="Mobiles",
                image_file="iphone.jpg"
            ),
            Product(
                name="Samsung Galaxy S24 Ultra",
                description="Powerhouse Android smartphone with AI features, integrated S-Pen, and stunning display.",
                price=1099.00, stock=12, category="Electronics", subcategory="Mobiles",
                image_file="samsung.jpg"
            ),
            Product(
                name="Noise Cancelling Headphones",
                description="Wireless over-ear headphones with premium sound quality and 30-hour battery life.",
                price=199.99, stock=25, category="Electronics", subcategory="Other",
                image_file="headphones.jpg"
            ),
            Product(
                name="iPad Pro 12.9 M2",
                description="The ultimate iPad experience with the world's most advanced mobile display.",
                price=999.00, stock=15, category="Electronics", subcategory="Tablets",
                image_file="https://images.unsplash.com/photo-1544244015-0df4b3ffc6b0?auto=format&fit=crop&w=500&q=80"
            ),

            # --- MEN'S FASHION ---
            Product(
                name="Men's Slim-Fit Denim Jeans",
                description="Classic blue slim-fit jeans made from premium durable denim. Perfect for casual wear.",
                price=59.00, stock=20, category="Men's Fashion", subcategory="Apparel",
                image_file="https://images.unsplash.com/photo-1542272604-787c3835535d?auto=format&fit=crop&w=500&q=80"
            ),
            Product(
                name="Premium White Oxford Shirt",
                description="100% Cotton Oxford shirt. Breathable and perfect for formal or business-casual settings.",
                price=45.00, stock=25, category="Men's Fashion", subcategory="Apparel",
                image_file="https://images.unsplash.com/photo-1521572163474-6864f9cf17ab?auto=format&fit=crop&w=500&q=80"
            ),
            Product(
                name="Casual Graphic T-Shirt",
                description="Soft cotton blend t-shirt with a modern minimalist design.",
                price=25.00, stock=40, category="Men's Fashion", subcategory="Apparel",
                image_file="https://images.unsplash.com/photo-1521572163474-6864f9cf17ab?auto=format&fit=crop&w=500&q=80"
            ),
            Product(
                name="Men's Formal Dress Pants",
                description="Sharp tailored formal pants in charcoal grey. Ideal for office and evening wear.",
                price=75.00, stock=15, category="Men's Fashion", subcategory="Apparel",
                image_file="https://images.unsplash.com/photo-1473966968600-fa801b869a1a?auto=format&fit=crop&w=500&q=80"
            ),
            Product(
                name="Classic Leather Jacket",
                description="Genuine leather jacket with a timeless design. Durable, stylish, and comfortable.",
                price=120.00, stock=15, category="Men's Fashion", subcategory="Apparel",
                image_file="https://images.unsplash.com/photo-1551028711-03057a484c0a?auto=format&fit=crop&w=500&q=80"
            ),

            # --- WOMEN'S FASHION ---
            Product(
                name="Elegant Silk Blouse",
                description="Lightweight silk blouse in cream. A versatile piece for your professional wardrobe.",
                price=85.00, stock=15, category="Women's Fashion", subcategory="Apparel",
                image_file="https://images.unsplash.com/photo-1564584217132-2271feaeb3c5?auto=format&fit=crop&w=500&q=80"
            ),
            Product(
                name="High-Waisted Skinny Jeans",
                description="Perfect fit high-waisted jeans with stretch denim for all-day comfort.",
                price=65.00, stock=30, category="Women's Fashion", subcategory="Apparel",
                image_file="https://images.unsplash.com/photo-1541099649105-f69ad21f3246?auto=format&fit=crop&w=500&q=80"
            ),
            Product(
                name="Floral Summer Mid-Dress",
                description="Beautiful floral print dress made from sustainable viscose.",
                price=89.00, stock=12, category="Women's Fashion", subcategory="Apparel",
                image_file="https://images.unsplash.com/photo-1515372039744-b8f02a3ae446?auto=format&fit=crop&w=500&q=80"
            ),
            Product(
                name="Ladies' Formal Blazer",
                description="Tailored black blazer with a modern cut. Perfect for power-dressing.",
                price=110.00, stock=10, category="Women's Fashion", subcategory="Apparel",
                image_file="https://images.unsplash.com/photo-1591047139829-d91aecb6caea?auto=format&fit=crop&w=500&q=80"
            ),
            Product(
                name="Casual Cotton Top",
                description="Breezy and comfortable cotton top for everyday elegance.",
                price=35.00, stock=45, category="Women's Fashion", subcategory="Apparel",
                image_file="https://images.unsplash.com/photo-1618354691792-d1d42acfd860?auto=format&fit=crop&w=500&q=80"
            ),

            # --- GROCERIES ---
            # --- GROCERIES: Fruits & Vegetables ---
            Product(
                name="Fresh Organic Bananas",
                description="Naturally ripened premium organic bananas. Rich in potassium and perfect for a healthy snack.",
                price=3.99, stock=50, category="Groceries", subcategory="Fruits & Vegetables", 
                image_file="https://images.unsplash.com/photo-1603833665858-e61d17a86224?auto=format&fit=crop&w=500&q=80"
            ),
            Product(
                name="Exotic Dragon Fruit",
                description="Vibrant and refreshing exotic pitaya. A powerhouse of antioxidants and fiber.",
                price=5.50, stock=20, category="Groceries", subcategory="Fruits & Vegetables", 
                image_file="https://images.unsplash.com/photo-1527325678964-54921661f888?auto=format&fit=crop&w=500&q=80"
            ),
            Product(
                name="Hydroponic Bell Peppers",
                description="Crisp and colorful combo of red, yellow, and green bell peppers.",
                price=4.25, stock=30, category="Groceries", subcategory="Fruits & Vegetables", 
                image_file="https://images.unsplash.com/photo-1566576721346-d4a3b4eaad5b?auto=format&fit=crop&w=500&q=80"
            ),

            # --- GROCERIES: Dairy & Bakery ---
            Product(
                name="Farm Fresh Whole Milk",
                description="Creamy, pasteurized whole milk from grass-fed cows. High in calcium.",
                price=4.50, stock=40, category="Groceries", subcategory="Dairy & Bakery", 
                image_file="https://images.unsplash.com/photo-1563636619-e9107da4a1bb?auto=format&fit=crop&w=500&q=80"
            ),
            Product(
                name="Artisanal Sourdough Bread",
                description="Freshly baked organic sourdough bread with a perfect crust and tangy flavor.",
                price=6.99, stock=15, category="Groceries", subcategory="Dairy & Bakery", 
                image_file="https://images.unsplash.com/photo-1585478259715-876a6a81fc08?auto=format&fit=crop&w=500&q=80"
            ),
            Product(
                name="Gourmet Greek Yogurt",
                description="Thick and creamy plain Greek yogurt. perfect for breakfast or smoothies.",
                price=5.99, stock=25, category="Groceries", subcategory="Dairy & Bakery", 
                image_file="https://images.unsplash.com/photo-1488477181946-6428a0291777?auto=format&fit=crop&w=500&q=80"
            ),

            # --- GROCERIES: Staples & Grains ---
            Product(
                name="Basmati King Rice",
                description="Premium extra-long grain aged Basmati rice with exquisite aroma.",
                price=15.99, stock=35, category="Groceries", subcategory="Staples & Grains", 
                image_file="https://images.unsplash.com/photo-1586201375761-83865001e31c?auto=format&fit=crop&w=500&q=80"
            ),
            Product(
                name="Cold Pressed Sunflower Oil",
                description="100% natural cold pressed oil, perfect for healthy cooking and frying.",
                price=12.50, stock=20, category="Groceries", subcategory="Staples & Grains", 
                image_file="https://images.unsplash.com/photo-1474979266404-7eaacbcd87c5?auto=format&fit=crop&w=500&q=80"
            ),

            # --- GROCERIES: Snacks & Packaged Foods ---
            Product(
                name="Organic Salted Kettle Chips",
                description="Thick-cut, hand-cooked potato chips seasoned with sea salt.",
                price=3.49, stock=60, category="Groceries", subcategory="Snacks & Packaged Foods", 
                image_file="https://images.unsplash.com/photo-1566478431375-7042f1abc3dd?auto=format&fit=crop&w=500&q=80"
            ),
            Product(
                name="Premium Choco-Chip Biscuits",
                description="Crunchy butter biscuits loaded with rich dark chocolate chips.",
                price=4.99, stock=45, category="Groceries", subcategory="Snacks & Packaged Foods", 
                image_file="https://images.unsplash.com/photo-1558961363-fa8fdf82db35?auto=format&fit=crop&w=500&q=80"
            ),

            # --- GROCERIES: Beverages ---
            Product(
                name="Cold Brew Coffee Concentrate",
                description="Smooth, low-acid cold brew coffee made from premium Arabica beans.",
                price=14.00, stock=30, category="Groceries", subcategory="Beverages", 
                image_file="https://images.unsplash.com/photo-1544145945-f904253db0ad?auto=format&fit=crop&w=500&q=80"
            ),
            Product(
                name="Hibiscus Herbal Tea",
                description="Refreshing caffeine-free herbal tea with a bright floral flavor.",
                price=8.99, stock=40, category="Groceries", subcategory="Beverages", 
                image_file="https://images.unsplash.com/photo-1576092768241-dec231879fc3?auto=format&fit=crop&w=500&q=80"
            ),

            # --- GROCERIES: Spices & Condiments ---
            Product(
                name="Manuka Honey MGO 250+",
                description="Certified premium Manuka honey from New Zealand. Great for wellness.",
                price=35.00, stock=15, category="Groceries", subcategory="Spices & Condiments", 
                image_file="https://images.unsplash.com/photo-1587049352846-4a222e784d38?auto=format&fit=crop&w=500&q=80"
            ),
            Product(
                name="Organic Turmeric Powder",
                description="High-curcumin turmeric powder, cold-ground to preserve nutrients.",
                price=6.50, stock=50, category="Groceries", subcategory="Spices & Condiments", 
                image_file="https://images.unsplash.com/photo-1615485290382-441e4d0c9cb5?auto=format&fit=crop&w=500&q=80"
            ),

            # --- GROCERIES: Personal Care ---
            Product(
                name="Lavender Essential Oil Soap",
                description="Handmade vegan soap with organic lavender oil and shea butter.",
                price=7.99, stock=40, category="Groceries", subcategory="Personal Care", 
                image_file="https://images.unsplash.com/photo-1600857062241-99e5ad747c94?auto=format&fit=crop&w=500&q=80"
            ),
            Product(
                name="Natural Bamboo Toothbrush",
                description="Eco-friendly bamboo toothbrush with charcoal-infused soft bristles.",
                price=4.50, stock=100, category="Groceries", subcategory="Personal Care", 
                image_file="https://images.unsplash.com/photo-1607613009820-a29f7bb81c04?auto=format&fit=crop&w=500&q=80"
            ),

            # --- HOME & KITCHEN: Kitchen & Dining ---
            Product(
                name="Premium Non-Stick Cookware Set",
                description="8-piece ceramic coated non-stick pans and pots. Induction friendly and dishwasher safe.",
                price=149.99, stock=15, category="Home & Kitchen", subcategory="Kitchen & Dining",
                image_file="https://images.unsplash.com/photo-1584990333910-fe90760aa009?auto=format&fit=crop&w=500&q=80"
            ),
            Product(
                name="Modern 16-Piece Dinnerware",
                description="Elegant matte finish stoneware set. Includes plates, bowls, and mugs for 4 people.",
                price=89.00, stock=20, category="Home & Kitchen", subcategory="Kitchen & Dining",
                image_file="https://images.unsplash.com/photo-1577114954203-7ed123992167?auto=format&fit=crop&w=500&q=80"
            ),

            # --- HOME & KITCHEN: Kitchen Storage ---
            Product(
                name="Airtight Food Container Set",
                description="Set of 12 BPA-free plastic containers with easy-lock lids for pantry organization.",
                price=39.99, stock=40, category="Home & Kitchen", subcategory="Kitchen Storage",
                image_file="https://images.unsplash.com/photo-1584622650111-993a426fbf0a?auto=format&fit=crop&w=500&q=80"
            ),
            Product(
                name="Bamboo Spice Rack Organizer",
                description="3-tier expandable spice rack for kitchen cabinets or countertops.",
                price=24.50, stock=25, category="Home & Kitchen", subcategory="Kitchen Storage",
                image_file="https://images.unsplash.com/photo-1590735204425-277d84229d60?auto=format&fit=crop&w=500&q=80"
            ),

            # --- HOME & KITCHEN: Home Décor ---
            Product(
                name="Minimalist Ceramic Vase Set",
                description="Set of 3 hand-crafted ceramic vases in neutral tones. Perfect for modern home decor.",
                price=45.00, stock=30, category="Home & Kitchen", subcategory="Home Décor",
                image_file="https://images.unsplash.com/photo-1581783898377-1c85bf937427?auto=format&fit=crop&w=500&q=80"
            ),
            Product(
                name="Framed Abstract Wall Art",
                description="Gallery-quality canvas print with a sleek black wood frame.",
                price=65.00, stock=15, category="Home & Kitchen", subcategory="Home Décor",
                image_file="https://images.unsplash.com/photo-1513519245088-0e12902e5a38?auto=format&fit=crop&w=500&q=80"
            ),

            # --- HOME & KITCHEN: Furniture ---
            Product(
                name="Ergonomic Cloud Sofa",
                description="Ultra-comfortable 3-seater sofa with premium upholstery and memory foam seating.",
                price=799.00, stock=5, category="Home & Kitchen", subcategory="Furniture",
                image_file="https://images.unsplash.com/photo-1555041469-a586c61ea9bc?auto=format&fit=crop&w=500&q=80"
            ),

            # --- HOME & KITCHEN: Home Cleaning ---
            Product(
                name="Smart Robotic Vacuum Cleaner",
                description="WiFi-enabled robot vacuum with mapping technology and powerful suction.",
                price=299.00, stock=10, category="Home & Kitchen", subcategory="Home Cleaning",
                image_file="https://images.unsplash.com/photo-1518640467707-6811f4a6ab73?auto=format&fit=crop&w=500&q=80"
            ),

            # --- HOME & KITCHEN: Small Appliances ---
            Product(
                name="Professional High-Speed Blender",
                description="1200W motor for smoothies, soups, and crushing ice with ease.",
                price=119.99, stock=20, category="Home & Kitchen", subcategory="Small Appliances",
                image_file="https://images.unsplash.com/photo-1585238341267-1cfec2046a55?auto=format&fit=crop&w=500&q=80"
            ),

            # --- HEALTH & FITNESS: Gym Equipment ---
            Product(
                name="Adjustable Dumbbell Set (Pair)",
                description="Quick-dial dumbbells ranging from 5 to 52.5 lbs. Space-saving fitness gear.",
                price=349.00, stock=12, category="Health & Fitness", subcategory="Gym Equipment",
                image_file="https://images.unsplash.com/photo-1583454110551-21f2fa2afe61?auto=format&fit=crop&w=500&q=80"
            ),
            Product(
                name="Heavy Duty Weight Bench",
                description="Adjustable incline/decline bench for full-body strength training.",
                price=159.00, stock=8, category="Health & Fitness", subcategory="Gym Equipment",
                image_file="https://images.unsplash.com/photo-1534438327276-14e5300c3a48?auto=format&fit=crop&w=500&q=80"
            ),

            # --- HEALTH & FITNESS: Cardio Equipment ---
            Product(
                name="Folding Electric Treadmill",
                description="Space-saving design with 12 preset workouts and integrated heart rate monitor.",
                price=499.00, stock=6, category="Health & Fitness", subcategory="Cardio Equipment",
                image_file="https://images.unsplash.com/photo-1540497077202-7c8a3999166f?auto=format&fit=crop&w=500&q=80"
            ),

            # --- HEALTH & FITNESS: Yoga & Meditation ---
            Product(
                name="Extra Thick Eco Yoga Mat",
                description="Non-slip natural rubber mat with alignment lines for perfect form.",
                price=48.00, stock=30, category="Health & Fitness", subcategory="Yoga & Meditation",
                image_file="https://images.unsplash.com/photo-1592432678016-bc94dbbf204e?auto=format&fit=crop&w=500&q=80"
            ),

            # --- HEALTH & FITNESS: Supplements ---
            Product(
                name="Premium Whey Protein Isolate",
                description="Low-carb, fast-absorbing protein powder for muscle recovery. 2kg Tub.",
                price=55.00, stock=25, category="Health & Fitness", subcategory="Supplements",
                image_file="https://images.unsplash.com/photo-1593095117211-12a0237da829?auto=format&fit=crop&w=500&q=80"
            ),

            # --- KIDS: Baby Care ---
            Product(
                name="Ultra-Soft Baby Bath Towel Set",
                description="Set of 3 organic bamboo towels. Gentle on sensitive baby skin.",
                price=24.99, stock=35, category="Kids", subcategory="Baby Care",
                image_file="https://images.unsplash.com/photo-1522771917714-d73ca5530182?auto=format&fit=crop&w=500&q=80"
            ),

            # --- KIDS: Educational Toys ---
            Product(
                name="STEM Solar Robot Kit",
                description="12-in-1 solar powered robot building set for kids aged 10+.",
                price=34.99, stock=20, category="Kids", subcategory="Educational Toys",
                image_file="https://images.unsplash.com/photo-1531210483974-4f8c1f33fd35?auto=format&fit=crop&w=500&q=80"
            ),
            Product(
                name="Wooden Alphabet Puzzle",
                description="Colorful 26-piece wooden block set to help toddlers learn the ABCs.",
                price=19.99, stock=40, category="Kids", subcategory="Educational Toys",
                image_file="https://images.unsplash.com/photo-1587654780291-39c9404d746b?auto=format&fit=crop&w=500&q=80"
            ),

            # --- KIDS: Action & Remote Toys ---
            Product(
                name="High-Speed RC Drift Car",
                description="1:16 scale remote control car with LED headlights and interchangeable tires.",
                price=45.00, stock=15, category="Kids", subcategory="Action & Remote Toys",
                image_file="https://images.unsplash.com/photo-1594787318286-3d835c1d207f?auto=format&fit=crop&w=500&q=80"
            )
        ]

        for p in products:
            db.session.add(p)
        
        db.session.commit()
        print("Global Multi-Category Database Seeded Successfully!")

if __name__ == "__main__":
    seed_data()
