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
                description="High-performance 14-inch laptop with 16GB RAM and 512GB SSD. Perfect for professionals.",
                price=899 * 80.0, stock=10, category="Electronics", subcategory="Laptops",
                image_file="laptop.jpg"
            ),
            Product(
                name="Dell Inspiron 15 Plus",
                description="Reliable 15-inch laptop with latest Gen Intel core processors.",
                price=749 * 80.0, stock=15, category="Electronics", subcategory="Laptops",
                image_file="laptop1.jpg"
            ),
            Product(
                name="HP Pavilion 14 Aero",
                description="Ultra-lightweight laptop, perfect for on-the-go productivity.",
                price=699 * 80.0, stock=20, category="Electronics", subcategory="Laptops",
                image_file="laptop2.jpg"
            ),
            Product(
                name="Lenovo ThinkPad X1 Carbon",
                description="Premium business laptop with incredible keyboard and durability.",
                price=1299 * 80.0, stock=10, category="Electronics", subcategory="Laptops",
                image_file="laptop3.jpg"
            ),
            Product(
                name="Asus ROG Zephyrus G14",
                description="High-end gaming laptop packed with an RTX graphics card.",
                price=1499 * 80.0, stock=8, category="Electronics", subcategory="Laptops",
                image_file="laptop4.jpg"
            ),
            Product(
                name="Acer Swift 3 OLED",
                description="Affordable and stunning OLED display laptop for creators.",
                price=799 * 80.0, stock=12, category="Electronics", subcategory="Laptops",
                image_file="laptop5.jpg"
            ),
            Product(
                name="Apple MacBook Air M1",
                description="The ultimate value fanless Apple laptop with all-day battery life.",
                price=899 * 80.0, stock=20, category="Electronics", subcategory="Laptops",
                image_file="makbook1.jpg"
            ),
            Product(
                name="Apple MacBook Pro 14 M2",
                description="Pro powerhouse with stunning Liquid Retina XDR display.",
                price=1999 * 80.0, stock=15, category="Electronics", subcategory="Laptops",
                image_file="mackbook2.jpg"
            ),
            Product(
                name="Apple MacBook Air M2",
                description="Redesigned ultra-thin Apple silicon MacBook with MagSafe.",
                price=1199 * 80.0, stock=10, category="Electronics", subcategory="Laptops",
                image_file="mackbook3.jpg"
            ),
            Product(
                name="Apple MacBook Pro 16 M3 Max",
                description="The most advanced Apple laptop for serious professional workflows.",
                price=2499 * 80.0, stock=5, category="Electronics", subcategory="Laptops",
                image_file="mackbook4.jpg"
            ),
            Product(
                name="Apple MacBook Studio Workstation",
                description="High-end workstation class portable machine.",
                price=2099 * 80.0, stock=8, category="Electronics", subcategory="Laptops",
                image_file="mackbook5.jpg"
            ),

            Product(
                name="iPhone 15 Pro Max",
                description="Ultimate flagship smartphone with titanium body, A17 Pro chip, and advanced camera system.",
                price=1199 * 80.0, stock=8, category="Electronics", subcategory="Mobiles",
                image_file="iphone.jpg"
            ),
            Product(
                name="Samsung Galaxy S24 Ultra",
                description="Powerhouse Android smartphone with AI features, integrated S-Pen, and stunning display.",
                price=1099 * 80.0, stock=12, category="Electronics", subcategory="Mobiles",
                image_file="samsung.jpg"
            ),
            Product(
                name="Samsung Galaxy S25",
                description="Next-generation flagship from Samsung with improved battery and cameras.",
                price=899 * 80.0, stock=15, category="Electronics", subcategory="Mobiles",
                image_file="GalaxyS25.jpg"
            ),
            Product(
                name="Samsung Galaxy S25 Ultra",
                description="The absolute pinnacle of Samsung smartphone engineering with unparalleled zoom capabilities.",
                price=1299 * 80.0, stock=10, category="Electronics", subcategory="Mobiles",
                image_file="GalaxyUltra.jpg"
            ),
            Product(
                name="Google Pixel 8 Pro",
                description="The pure Android experience with the best and smartest AI camera on the market.",
                price=999 * 80.0, stock=18, category="Electronics", subcategory="Mobiles",
                image_file="GooglePixel.jpg"
            ),
            Product(
                name="OnePlus 12 5G",
                description="Smooth beyond belief with massive battery and fastest charging speeds.",
                price=799 * 80.0, stock=20, category="Electronics", subcategory="Mobiles",
                image_file="mob1.jpg"
            ),
            Product(
                name="Xiaomi 14 Pro Leica Edition",
                description="Premium mobile with Leica co-engineered cameras.",
                price=849 * 80.0, stock=12, category="Electronics", subcategory="Mobiles",
                image_file="mobiles.jpg"
            ),
            Product(
                name="Vivo X100 Pro ZEISS",
                description="Photography powerhouse phone perfect for portrait photography.",
                price=899 * 80.0, stock=10, category="Electronics", subcategory="Mobiles",
                image_file="vivo1.jpg"
            ),

            Product(
                name="Apple iPad Air M1",
                description="Light, thin and incredibly capable tablet for all your daily needs.",
                price=599 * 80.0, stock=20, category="Electronics", subcategory="Tablets",
                image_file="tablet1.jpg"
            ),
            Product(
                name="Samsung Galaxy Tab S9",
                description="Pro-grade Android tablet with AMOLED 120Hz display.",
                price=799 * 80.0, stock=15, category="Electronics", subcategory="Tablets",
                image_file="tablets.jpg"
            ),
            Product(
                name="Lenovo Tab P12 Pro",
                description="Thin and light Android pad with great audio and screen for media.",
                price=499 * 80.0, stock=25, category="Electronics", subcategory="Tablets",
                image_file="tablets3.jpg"
            ),

            Product(
                name="Noise Cancelling Headphones",
                description="Wireless over-ear headphones with premium sound quality and 30-hour battery life.",
                price=199 * 80.0, stock=25, category="Electronics", subcategory="Other",
                image_file="headphones.jpg"
            ),
            Product(
                name="Razer Kraken V3 Gaming Headset",
                description="Immersive gaming headset with multi-platform compatibility and haptic feedback.",
                price=129 * 80.0, stock=30, category="Electronics", subcategory="Other",
                image_file="headset.jpg"
            ),
            Product(
                name="Sony WF-1000XM5 Earbuds",
                description="The industry leading true wireless noise cancelling earbuds.",
                price=298 * 80.0, stock=25, category="Electronics", subcategory="Other",
                image_file="other2.jpg"
            ),
            Product(
                name="Apple Watch Series 9",
                description="Smarter. Brighter. Mightier health/fitness companion.",
                price=399 * 80.0, stock=40, category="Electronics", subcategory="Other",
                image_file="other4.jpg"
            ),
            Product(
                name="JBL Flip 6 Bluetooth Speaker",
                description="Portable waterproof speaker with surprisingly powerful sound.",
                price=129 * 80.0, stock=20, category="Electronics", subcategory="Other",
                image_file="others1.jpg"
            ),
            Product(
                name="Logitech MX Master 3S Mouse",
                description="The ultimate precision mouse for creators and coders.",
                price=99 * 80.0, stock=50, category="Electronics", subcategory="Other",
                image_file="others5.jpg"
            ),

            # --- MEN'S FASHION ---
            Product(
                name="Men's Slim-Fit Denim Jeans",
                description="Classic blue slim-fit jeans made from premium durable denim. Perfect for casual wear.",
                price=59 * 80.0, stock=20, category="Men's Fashion", subcategory="Apparel",
                image_file="Mens/jeans1.jpg"
            ),
            Product(
                name="Premium White Oxford Shirt",
                description="100% Cotton Oxford shirt. Breathable and perfect for formal or business-casual settings.",
                price=45 * 80.0, stock=25, category="Men's Fashion", subcategory="Apparel",
                image_file="Mens/s1.jpg"
            ),
            Product(
                name="Casual Graphic T-Shirt",
                description="Soft cotton blend t-shirt with a modern minimalist design.",
                price=25 * 80.0, stock=40, category="Men's Fashion", subcategory="Apparel",
                image_file="Mens/t1.jpg"
            ),
            Product(
                name="Men's Formal Dress Pants",
                description="Sharp tailored formal pants in charcoal grey. Ideal for office and evening wear.",
                price=75 * 80.0, stock=15, category="Men's Fashion", subcategory="Apparel",
                image_file="Mens/fash1.jpg"
            ),
            Product(
                name="Classic Leather Jacket",
                description="Genuine leather jacket with a timeless design. Durable, stylish, and comfortable.",
                price=120 * 80.0, stock=15, category="Men's Fashion", subcategory="Apparel",
                image_file="Mens/fash2.jpg"
            ),
            Product(
                name="Distressed Casual Jeans",
                description="Trendy distressed jeans for an everyday modern look.",
                price=49 * 80.0, stock=30, category="Men's Fashion", subcategory="Apparel",
                image_file="Mens/jeans2.jpg"
            ),
            Product(
                name="Blue Striped Dress Shirt",
                description="Smart-casual striped dress shirt, excellent for business meetings.",
                price=55 * 80.0, stock=20, category="Men's Fashion", subcategory="Apparel",
                image_file="Mens/s2.jpg"
            ),
            Product(
                name="Solid Color Polo T-Shirt",
                description="Classic polo shirt in breathable cotton piqué material.",
                price=30 * 80.0, stock=50, category="Men's Fashion", subcategory="Apparel",
                image_file="Mens/t2.jpg"
            ),
            Product(
                name="Men's Stylish Chinos",
                description="Versatile and comfortable chinos perfect for bridging the gap between casual and formal.",
                price=55 * 80.0, stock=25, category="Men's Fashion", subcategory="Apparel",
                image_file="Mens/jeans3.jpg"
            ),
            Product(
                name="Winter Knit Sweater",
                description="Warm and cozy knit sweater designed for colder months.",
                price=65 * 80.0, stock=15, category="Men's Fashion", subcategory="Apparel",
                image_file="Mens/fash3.jpg"
            ),

            # --- WOMEN'S FASHION ---
            Product(
                name="Elegant Crepe Blouse",
                description="Lightweight crepe blouse in striking colors. A versatile piece for your professional wardrobe.",
                price=85 * 80.0, stock=15, category="Women's Fashion", subcategory="Apparel",
                image_file="Womens/c1.jpg"
            ),
            Product(
                name="High-Waisted Skinny Jeans",
                description="Perfect fit high-waisted jeans with stretch denim for all-day comfort.",
                price=65 * 80.0, stock=30, category="Women's Fashion", subcategory="Apparel",
                image_file="Womens/c3.jpg"
            ),
            Product(
                name="Floral Summer Mid-Dress",
                description="Beautiful floral print dress made from sustainable viscose.",
                price=89 * 80.0, stock=12, category="Women's Fashion", subcategory="Apparel",
                image_file="Womens/c4.jpg"
            ),
            Product(
                name="Ladies' Formal Blazer",
                description="Tailored smart blazer with a modern cut. Perfect for power-dressing.",
                price=110 * 80.0, stock=10, category="Women's Fashion", subcategory="Apparel",
                image_file="Womens/c5.jpg"
            ),
            Product(
                name="Designer Evening Top",
                description="Breezy and comfortable designer top for everyday elegance.",
                price=95 * 80.0, stock=45, category="Women's Fashion", subcategory="Apparel",
                image_file="Womens/fash1.jpg"
            ),
            Product(
                name="Stylish Trench Coat",
                description="Classic lightweight trench coat perfect for rainy and windy days.",
                price=140 * 80.0, stock=12, category="Women's Fashion", subcategory="Apparel",
                image_file="Womens/fash2.jpg"
            ),
            Product(
                name="Chic Pleated Skirt",
                description="Elegant pleated midi skirt that goes perfectly with formal tops.",
                price=55 * 80.0, stock=24, category="Women's Fashion", subcategory="Apparel",
                image_file="Womens/fash3.jpg"
            ),
            Product(
                name="Bohemian Print Top",
                description="Loose-fitting bohemian top with vibrant prints.",
                price=45 * 80.0, stock=35, category="Women's Fashion", subcategory="Apparel",
                image_file="Womens/fash5.jpg"
            ),
            Product(
                name="Women's Formal Suit",
                description="Complete smart suit for the modern businesswoman.",
                price=160 * 80.0, stock=10, category="Women's Fashion", subcategory="Apparel",
                image_file="Womens/s1.jpg"
            ),
            Product(
                name="Casual Summer Tee",
                description="Breathable soft cotton T-shirt designed specially for comfort.",
                price=30 * 80.0, stock=50, category="Women's Fashion", subcategory="Apparel",
                image_file="Womens/t1.jpg"
            ),


            # --- GROCERIES ---
            # --- GROCERIES: Fruits & Vegetables ---
            Product(name="Fresh Black & White Orange", description="Premium imported oranges.", price=6.50 * 80.0, stock=50, category="Groceries", subcategory="Fruits & Vegetables", image_file="fruits&Vegetables/B&W Orange.jpg"),
            Product(name="Exotic Black Orange", description="Rare variety extra sweet oranges.", price=8.00 * 80.0, stock=20, category="Groceries", subcategory="Fruits & Vegetables", image_file="fruits&Vegetables/BlackOrange.jpg"),
            Product(name="Mixed Fruit Basket", description="A beautiful basket of fresh mixed fruits.", price=20.00 * 80.0, stock=15, category="Groceries", subcategory="Fruits & Vegetables", image_file="fruits&Vegetables/BucketFruit.jpg"),
            Product(name="Farm Fresh Apples", description="Sweet and nutritious farm fresh apples.", price=4.99 * 80.0, stock=50, category="Groceries", subcategory="Fruits & Vegetables", image_file="fruits&Vegetables/FreshApple.jpg"),
            Product(name="Assorted Mixed Fruits", description="A combination of daily essential sweet fruits.", price=15.00 * 80.0, stock=30, category="Groceries", subcategory="Fruits & Vegetables", image_file="fruits&Vegetables/MixFruits.jpg"),
            Product(name="Farm Fresh Mixed Vegetables", description="Daily essential fresh vegetables including greens.", price=8.99 * 80.0, stock=40, category="Groceries", subcategory="Fruits & Vegetables", image_file="fruits&Vegetables/MixVeg.jpg"),
            Product(name="Fresh Pomegranate", description="Rich antioxidant pomegranates.", price=7.50 * 80.0, stock=25, category="Groceries", subcategory="Fruits & Vegetables", image_file="fruits&Vegetables/Pom.jpg"),
            Product(name="Fresh Apple Tree Picks", description="Straight from the apple trees, crisp and delicious.", price=12.00 * 80.0, stock=20, category="Groceries", subcategory="Fruits & Vegetables", image_file="fruits&Vegetables/apple trees.jpg"),
            Product(name="Organic Brinjal (Eggplant)", description="Freshly picked organic brinjal for your daily cooking.", price=3.50 * 80.0, stock=50, category="Groceries", subcategory="Fruits & Vegetables", image_file="fruits&Vegetables/brinjal.jpg"),
            Product(name="Crunchy Organic Carrots", description="Sweet and crunchy orange carrots.", price=2.99 * 80.0, stock=60, category="Groceries", subcategory="Fruits & Vegetables", image_file="fruits&Vegetables/carrot.jpg"),
            Product(name="Fresh Hydrating Cucumbers", description="Perfect crisp cucumbers for salads.", price=2.50 * 80.0, stock=55, category="Groceries", subcategory="Fruits & Vegetables", image_file="fruits&Vegetables/cucumber.jpg"),
            Product(name="Organic Mixed Greens", description="Fresh and leafy green vegetables.", price=5.50 * 80.0, stock=40, category="Groceries", subcategory="Fruits & Vegetables", image_file="fruits&Vegetables/freshveg.jpg"),
            Product(name="Fresh Sweet Guava", description="Delicious sweet and soft guavas.", price=4.20 * 80.0, stock=30, category="Groceries", subcategory="Fruits & Vegetables", image_file="fruits&Vegetables/guava.jpg"),
            Product(name="Raw Jackfruit (Kathal)", description="Freshly cut raw jackfruit ready for cooking.", price=6.50 * 80.0, stock=15, category="Groceries", subcategory="Fruits & Vegetables", image_file="fruits&Vegetables/kathal.jpg"),
            Product(name="Sweet Alphonso Mangoes", description="The king of fruits, sweet and aromatic mangoes.", price=12.50 * 80.0, stock=25, category="Groceries", subcategory="Fruits & Vegetables", image_file="fruits&Vegetables/mango.jpg"),
            Product(name="Fresh Citrus Oranges", description="Juicy and tangy classic oranges.", price=5.50 * 80.0, stock=45, category="Groceries", subcategory="Fruits & Vegetables", image_file="fruits&Vegetables/orange.jpg"),
            Product(name="Ripe Organic Papaya", description="Soft, sweet and highly nutritious papaya.", price=4.50 * 80.0, stock=20, category="Groceries", subcategory="Fruits & Vegetables", image_file="fruits&Vegetables/papaya.jpg"),
            Product(name="Fresh Green Capsicum", description="Crunchy green capsicum for your stir-fries.", price=3.80 * 80.0, stock=40, category="Groceries", subcategory="Fruits & Vegetables", image_file="fruits&Vegetables/simla.jpg"),

            # --- GROCERIES: Dairy & Bakery ---
            Product(name="Refreshing Masala Chaas", description="Traditional spiced buttermilk for cooling down.", price=2.50 * 80.0, stock=30, category="Groceries", subcategory="Dairy & Bakery", image_file="Dairy&Bakery/Masala Chaas.jpg"),
            Product(name="Assorted Bakery Items", description="Freshly baked breads and buns.", price=8.99 * 80.0, stock=20, category="Groceries", subcategory="Dairy & Bakery", image_file="Dairy&Bakery/bakery.jpg"),
            Product(name="Fresh Baked Buns", description="Soft and fluffy bakery buns.", price=4.50 * 80.0, stock=25, category="Groceries", subcategory="Dairy & Bakery", image_file="Dairy&Bakery/bakeryprod1.jpg"),
            Product(name="Creamy Farm Butter", description="Rich and creamy old-fashioned butter.", price=6.00 * 80.0, stock=40, category="Groceries", subcategory="Dairy & Bakery", image_file="Dairy&Bakery/butter.jpg"),
            Product(name="Classic Buttermilk", description="Pure unsweetened buttermilk.", price=3.00 * 80.0, stock=35, category="Groceries", subcategory="Dairy & Bakery", image_file="Dairy&Bakery/buttermilk.jpg"),
            Product(name="Premium Cheese & Butter", description="Gourmet cheese block paired with fresh butter.", price=10.00 * 80.0, stock=15, category="Groceries", subcategory="Dairy & Bakery", image_file="Dairy&Bakery/cheeseButter.jpg"),
            Product(name="Rich Chocolate Cake", description="Decadent and moist dark chocolate cake.", price=18.00 * 80.0, stock=10, category="Groceries", subcategory="Dairy & Bakery", image_file="Dairy&Bakery/choccake.jpg"),
            Product(name="Fresh Dairy Milk", description="Nutritious pure cow's milk.", price=4.00 * 80.0, stock=50, category="Groceries", subcategory="Dairy & Bakery", image_file="Dairy&Bakery/dairymilk.jpg"),
            Product(name="Homemade Style Bread", description="Rustic and hearty homemade-style loaf.", price=5.50 * 80.0, stock=20, category="Groceries", subcategory="Dairy & Bakery", image_file="Dairy&Bakery/domowy.jpg"),
            Product(name="Traditional Matka Dahi", description="Thick curd traditionally set in a clay pot.", price=5.00 * 80.0, stock=30, category="Groceries", subcategory="Dairy & Bakery", image_file="Dairy&Bakery/matka dhau.jpg"),
            Product(name="Rolled Butter", description="Soft gourmet butter roll.", price=7.50 * 80.0, stock=25, category="Groceries", subcategory="Dairy & Bakery", image_file="Dairy&Bakery/rollbutter.jpg"),
            Product(name="Traditional Cheesecake (Sernik)", description="Classic sweet cheesecake slice.", price=15.00 * 80.0, stock=12, category="Groceries", subcategory="Dairy & Bakery", image_file="Dairy&Bakery/sernik.jpg"),

            # --- GROCERIES: Staples & Grains ---
            Product(name="Mixed Whole Grains", description="Assorted whole grains mix fresh from the mills.", price=9.00 * 80.0, stock=40, category="Groceries", subcategory="Staples & Grains", image_file="Staples&Grains/Grain Mills.jpg"),
            Product(name="Shuddh Dharohar Whole Wheat", description="Pure quality whole wheat grains.", price=12.50 * 80.0, stock=35, category="Groceries", subcategory="Staples & Grains", image_file="Staples&Grains/Shuddh Dharohar.jpg"),
            Product(name="Assorted Grains Pack", description="A premium blend of nutritional grains.", price=15.00 * 80.0, stock=25, category="Groceries", subcategory="Staples & Grains", image_file="Staples&Grains/allgrains.jpg"),
            Product(name="Premium Mixed Nuts", description="Healthy combination of almonds, cashews, and walnuts.", price=22.00 * 80.0, stock=50, category="Groceries", subcategory="Staples & Grains", image_file="Staples&Grains/nuts.jpg"),
            Product(name="Organic Mixed Pulses", description="Protein-rich dal and pulses mix.", price=8.50 * 80.0, stock=45, category="Groceries", subcategory="Staples & Grains", image_file="Staples&Grains/pulses.jpg"),
            Product(name="Premium Red Rajma", description="Large sized kidney beans for the perfect curry.", price=7.50 * 80.0, stock=40, category="Groceries", subcategory="Staples & Grains", image_file="Staples&Grains/rajma.jpg"),
            Product(name="Organic Wheat Grains", description="Golden organic wheat kernels.", price=10.00 * 80.0, stock=30, category="Groceries", subcategory="Staples & Grains", image_file="Staples&Grains/wheat.jpg"),

            # --- GROCERIES: Beverages ---
            Product(name="Premium Coffee Splash", description="Iced coffee delight with a refreshing splash.", price=6.50 * 80.0, stock=25, category="Groceries", subcategory="Beverages", image_file="Beverages/Coffee Splash.jpg"),
            Product(name="Heineken Non-Alcoholic Beer", description="Great tasting non-alcoholic malt beverage.", price=12.00 * 80.0, stock=30, category="Groceries", subcategory="Beverages", image_file="Beverages/Tasted Heineken.jpg"),
            Product(name="Al Ain Mineral Water", description="Pure and refreshing bottled mineral water.", price=2.00 * 80.0, stock=100, category="Groceries", subcategory="Beverages", image_file="Beverages/alain.jpg"),
            Product(name="Assorted Cold Beverages", description="Enjoy a mix of colorful refreshing drinks.", price=10.00 * 80.0, stock=40, category="Groceries", subcategory="Beverages", image_file="Beverages/beverages.jpg"),
            Product(name="Mocktail Mix", description="Fruity mocktail mixture for your get-togethers.", price=8.50 * 80.0, stock=35, category="Groceries", subcategory="Beverages", image_file="Beverages/cocktail.jpg"),
            Product(name="Rich Arabica Coffee Beans", description="Roasted coffee beans for a perfect brew.", price=15.00 * 80.0, stock=50, category="Groceries", subcategory="Beverages", image_file="Beverages/coffee.jpg"),
            Product(name="Curvical Energy Drink", description="Boost your energy with this power beverage.", price=5.50 * 80.0, stock=60, category="Groceries", subcategory="Beverages", image_file="Beverages/curvical.jpg"),
            Product(name="Fresh Mint Mojito", description="Lime and mint flavored sparkling drink.", price=4.50 * 80.0, stock=45, category="Groceries", subcategory="Beverages", image_file="Beverages/mojito.jpg"),
            Product(name="Premium Herbal Tea", description="Soothing and relaxing tea leaves.", price=7.50 * 80.0, stock=55, category="Groceries", subcategory="Beverages", image_file="Beverages/tea.jpg"),

            # --- GROCERIES: Spices & Condiments ---
            Product(name="Favorite Spice Blends", description="A special mix of our best-selling spices.", price=12.00 * 80.0, stock=30, category="Groceries", subcategory="Spices & Condiments", image_file="Spices&Condiments/Favorite Spice Blends.jpg"),
            Product(name="Homemade Pickle/Spices", description="Traditional homemade style condiments.", price=9.50 * 80.0, stock=25, category="Groceries", subcategory="Spices & Condiments", image_file="Spices&Condiments/Homemade.jpg"),
            Product(name="Organic Cinnamon Sticks", description="Aromatic cinnamon for sweet and savory dishes.", price=8.00 * 80.0, stock=40, category="Groceries", subcategory="Spices & Condiments", image_file="Spices&Condiments/cinnanon.jpg"),
            Product(name="Premium Cloves (Laung)", description="Strong flavored, high-quality whole cloves.", price=10.50 * 80.0, stock=35, category="Groceries", subcategory="Spices & Condiments", image_file="Spices&Condiments/lawag.jpg"),
            Product(name="Fiery Red Chilli Powder", description="Bright and spicy red chilli powder.", price=6.50 * 80.0, stock=55, category="Groceries", subcategory="Spices & Condiments", image_file="Spices&Condiments/redchilli.jpg"),
            Product(name="Authentic Indian Masala", description="Rich and deeply colored spice powder for curries.", price=7.50 * 80.0, stock=50, category="Groceries", subcategory="Spices & Condiments", image_file="Spices&Condiments/spice2.jpg"),
            Product(name="Assorted Whole Spices", description="A beautiful assortment of whole Indian species.", price=15.00 * 80.0, stock=20, category="Groceries", subcategory="Spices & Condiments", image_file="Spices&Condiments/spices.jpg"),
            Product(name="Golden Turmeric Powder", description="Healthy and pure bright yellow turmeric.", price=5.50 * 80.0, stock=60, category="Groceries", subcategory="Spices & Condiments", image_file="Spices&Condiments/turmeric.jpg"),

            # --- GROCERIES: Personal Care ---
            Product(name="Bleu Men's Fragrance", description="A fresh and aromatic everyday perfume for men.", price=45.00 * 80.0, stock=20, category="Groceries", subcategory="Personal Care", image_file="Personal Care/Bleu.jpg"),
            Product(name="Premium Hair Care Kit", description="Shampoos and conditioners for all hair types.", price=25.00 * 80.0, stock=25, category="Groceries", subcategory="Personal Care", image_file="Personal Care/Hair Care.jpg"),
            Product(name="Classic Men's Cologne", description="Strong, long-lasting masculine scent.", price=40.00 * 80.0, stock=15, category="Groceries", subcategory="Personal Care", image_file="Personal Care/Men’s Cologne.jpg"),
            Product(name="Minimalist Skincare Set", description="Essential serums and creams for a healthy glow.", price=55.00 * 80.0, stock=10, category="Groceries", subcategory="Personal Care", image_file="Personal Care/MinimalSkincare.jpg"),
            Product(name="Natural Herbal Skincare", description="Organic and pure skincare elements.", price=35.00 * 80.0, stock=15, category="Groceries", subcategory="Personal Care", image_file="Personal Care/NaturalSkinCare.jpg"),
            Product(name="Assorted Floral Scents", description="A beautiful collection of floral perfumes.", price=30.00 * 80.0, stock=20, category="Groceries", subcategory="Personal Care", image_file="Personal Care/Scents.jpg"),
            Product(name="Daily Skincare Essentials", description="Moisturizers and cleansers for your daily routine.", price=45.00 * 80.0, stock=25, category="Groceries", subcategory="Personal Care", image_file="Personal Care/Skincare.jpg"),
            Product(name="YSL Luxury Perfume", description="Exclusive designer fragrance for special occasions.", price=85.00 * 80.0, stock=10, category="Groceries", subcategory="Personal Care", image_file="Personal Care/YSL.jpg"),
            Product(name="Avocado Extract Body Wash", description="Nourishing body wash with avocado essence.", price=18.00 * 80.0, stock=30, category="Groceries", subcategory="Personal Care", image_file="Personal Care/avacodo.jpg"),



            # --- HOME & KITCHEN ---
            # --- HOME & KITCHEN: Kitchen & Dining ---
            Product(name="Black Walnut Dining Table", description="Solid black walnut dining set for your elegant home.", price=349 * 80.0, stock=10, category="Home & Kitchen", subcategory="Kitchen & Dining", image_file="Home&Kitchen/Kitchen&Dining/BlackWalnutDining.jpg"),
            Product(name="Culinary Havens Set", description="A premium dining set for luxury culinary experiences.", price=499 * 80.0, stock=5, category="Home & Kitchen", subcategory="Kitchen & Dining", image_file="Home&Kitchen/Kitchen&Dining/CulinaryHavens.jpg"),
            Product(name="Modern Teakwood Table", description="Durable and classic teakwood dining table.", price=299 * 80.0, stock=8, category="Home & Kitchen", subcategory="Kitchen & Dining", image_file="Home&Kitchen/Kitchen&Dining/Modernteakwood.jpg"),
            Product(name="Dining & Kitchen Combined Set", description="Complete open-kitchen matching dining set.", price=599 * 80.0, stock=3, category="Home & Kitchen", subcategory="Kitchen & Dining", image_file="Home&Kitchen/Kitchen&Dining/dining&kitchenset.jpg"),
            Product(name="Classic Wooden Dining Table", description="A sturdy classic 6-seater wooden table.", price=249 * 80.0, stock=15, category="Home & Kitchen", subcategory="Kitchen & Dining", image_file="Home&Kitchen/Kitchen&Dining/diningtable.jpg"),
            Product(name="Glass Top Dining Table", description="Sleek glass top dining table with modern chairs.", price=399 * 80.0, stock=6, category="Home & Kitchen", subcategory="Kitchen & Dining", image_file="Home&Kitchen/Kitchen&Dining/diningtable2.jpg"),
            Product(name="Minimalist Dining Table", description="Simple, space-saving dining table design.", price=199 * 80.0, stock=20, category="Home & Kitchen", subcategory="Kitchen & Dining", image_file="Home&Kitchen/Kitchen&Dining/dinintable2.jpg"),
            Product(name="Complete Kitchen Set (Wood)", description="Beautiful wooden kitchen cabinetry and island.", price=1299 * 80.0, stock=2, category="Home & Kitchen", subcategory="Kitchen & Dining", image_file="Home&Kitchen/Kitchen&Dining/kitchenset.jpg"),
            Product(name="Marble Top Kitchen Set", description="Luxurious marble top island and kitchen cabinets.", price=1599 * 80.0, stock=2, category="Home & Kitchen", subcategory="Kitchen & Dining", image_file="Home&Kitchen/Kitchen&Dining/kitchenset2.jpg"),
            Product(name="Modern Minimalist Kitchen Set", description="Clean and modular minimalist kitchen.", price=899 * 80.0, stock=4, category="Home & Kitchen", subcategory="Kitchen & Dining", image_file="Home&Kitchen/Kitchen&Dining/kitchenset3.jpg"),
            Product(name="Rustic Farmhouse Kitchen Set", description="Cozy and traditional farmhouse-style kitchen setup.", price=1099 * 80.0, stock=3, category="Home & Kitchen", subcategory="Kitchen & Dining", image_file="Home&Kitchen/Kitchen&Dining/kitchenset4.jpg"),
            Product(name="Contemporary Dark Kitchen Set", description="Stylish dark-themed modern kitchen set.", price=1499 * 80.0, stock=1, category="Home & Kitchen", subcategory="Kitchen & Dining", image_file="Home&Kitchen/Kitchen&Dining/kitchenset5.jpg"),

            # --- HOME & KITCHEN: Home Décor ---
            Product(name="3D Printed Vase", description="Modern geometrically designed 3D printed vase.", price=45 * 80.0, stock=30, category="Home & Kitchen", subcategory="Home Décor", image_file="Home&Kitchen/HomeDecor/3Dprintvase.jpg"),
            Product(name="Premium Home Decor Pack", description="An essential collection of elegant home decor items.", price=120 * 80.0, stock=15, category="Home & Kitchen", subcategory="Home Décor", image_file="Home&Kitchen/HomeDecor/HomeDecor.jpg"),
            Product(name="Reader Sculpture", description="Artistic reading figure sculpture for your desk.", price=35 * 80.0, stock=25, category="Home & Kitchen", subcategory="Home Décor", image_file="Home&Kitchen/HomeDecor/READER.jpg"),
            Product(name="Yoga Pose Candle Set", description="Relaxing and aesthetic yoga pose candles.", price=25 * 80.0, stock=40, category="Home & Kitchen", subcategory="Home Décor", image_file="Home&Kitchen/HomeDecor/YogaPoseCandle.jpg"),
            Product(name="Wall Art Set", description="Set of complementary aesthetic wall frames.", price=75 * 80.0, stock=20, category="Home & Kitchen", subcategory="Home Décor", image_file="Home&Kitchen/HomeDecor/decor1.jpg"),
            Product(name="Ceramic Desk Planter", description="Beautiful small ceramic planter for indoor plants.", price=22 * 80.0, stock=35, category="Home & Kitchen", subcategory="Home Décor", image_file="Home&Kitchen/HomeDecor/decor2.jpg"),
            Product(name="Boho Macrame Wall Hanging", description="Handwoven boho macrame decor.", price=40 * 80.0, stock=20, category="Home & Kitchen", subcategory="Home Décor", image_file="Home&Kitchen/HomeDecor/decor3.jpg"),
            Product(name="Aesthetic Table Lamp", description="Modern aesthetic warm light table lamp.", price=85 * 80.0, stock=10, category="Home & Kitchen", subcategory="Home Décor", image_file="Home&Kitchen/HomeDecor/decor4.jpg"),
            Product(name="Metal Wall Clock", description="Retro large metal wall clock.", price=60 * 80.0, stock=18, category="Home & Kitchen", subcategory="Home Décor", image_file="Home&Kitchen/HomeDecor/decor5.jpg"),
            Product(name="Crystal Ornament Piece", description="Shiny and reflective decorative crystal ornament.", price=95 * 80.0, stock=12, category="Home & Kitchen", subcategory="Home Décor", image_file="Home&Kitchen/HomeDecor/decor6.jpg"),

            # --- HOME & KITCHEN: Furniture ---
            Product(name="Executive Leather Chair", description="Premium genuine leather chair for the office.", price=249 * 80.0, stock=10, category="Home & Kitchen", subcategory="Furniture", image_file="Home&Kitchen/Furniture/Leatherchair.jpg"),
            Product(name="3D Designed Accent Chair", description="Modern uniquely shaped living room chair.", price=189 * 80.0, stock=8, category="Home & Kitchen", subcategory="Furniture", image_file="Home&Kitchen/Furniture/Notebook3D.jpg"),
            Product(name="Cozy Fabric Sofas", description="Comfortable multi-seater fabric sofa setup.", price=599 * 80.0, stock=5, category="Home & Kitchen", subcategory="Furniture", image_file="Home&Kitchen/Furniture/Sofas.jpg"),
            Product(name="Wooden Accent Chair", description="Classic wooden frame chair with cushion.", price=149 * 80.0, stock=15, category="Home & Kitchen", subcategory="Furniture", image_file="Home&Kitchen/Furniture/fur1.jpg"),
            Product(name="Velvet Lounge Chair", description="Luxurious velvet finish lounge chair.", price=219 * 80.0, stock=12, category="Home & Kitchen", subcategory="Furniture", image_file="Home&Kitchen/Furniture/fur2.jpg"),
            Product(name="Minimalist Bookshelf", description="Tall wooden minimalist bookshelf.", price=129 * 80.0, stock=20, category="Home & Kitchen", subcategory="Furniture", image_file="Home&Kitchen/Furniture/fur4.jpg"),
            Product(name="Round Coffee Table", description="Aesthetic glass and wood round coffee table.", price=99 * 80.0, stock=25, category="Home & Kitchen", subcategory="Furniture", image_file="Home&Kitchen/Furniture/fur5.jpg"),
            Product(name="Modern TV Cabinet", description="Sleek and low-profile modern TV console.", price=199 * 80.0, stock=10, category="Home & Kitchen", subcategory="Furniture", image_file="Home&Kitchen/Furniture/fur6.jpg"),
            Product(name="Bedside Table", description="Compact wooden bedside stand.", price=49 * 80.0, stock=30, category="Home & Kitchen", subcategory="Furniture", image_file="Home&Kitchen/Furniture/furr6.jpg"),
            Product(name="Room Decor Guitar", description="Decorative acoustic guitar for a musical vibe.", price=89 * 80.0, stock=5, category="Home & Kitchen", subcategory="Furniture", image_file="Home&Kitchen/Furniture/guitar.jpg"),
            Product(name="Display Guitar Stand", description="Wooden floor stand suitable for displaying guitars.", price=29 * 80.0, stock=15, category="Home & Kitchen", subcategory="Furniture", image_file="Home&Kitchen/Furniture/guitar1.jpg"),

            # --- HOME & KITCHEN: Home Cleaning ---
            Product(name="Heavy Duty Vacuum Cleaner", description="Powerful vacuum cleaner for all surfaces.", price=199 * 80.0, stock=20, category="Home & Kitchen", subcategory="Home Cleaning", image_file="Home&Kitchen/HomeCleaning/cleaner.jpg"),
            Product(name="Cordless Stick Vacuum", description="Lightweight and battery-operated floor vacuum.", price=149 * 80.0, stock=15, category="Home & Kitchen", subcategory="Home Cleaning", image_file="Home&Kitchen/HomeCleaning/cleaner1.jpg"),
            Product(name="Advanced Robot Cleaner", description="Smart robotic vacuum equipped with mapping tech.", price=299 * 80.0, stock=10, category="Home & Kitchen", subcategory="Home Cleaning", image_file="Home&Kitchen/HomeCleaning/cleaner2.jpg"),
            Product(name="Wet & Dry Mop Vacuum", description="Hybrid cleaner for both sweeping and mopping.", price=249 * 80.0, stock=8, category="Home & Kitchen", subcategory="Home Cleaning", image_file="Home&Kitchen/HomeCleaning/cleaner4.jpg"),

            # --- HOME & KITCHEN: Small Appliances ---
            Product(name="Multi-Purpose Box Grater", description="Stainless steel 4-sided box grater.", price=15 * 80.0, stock=40, category="Home & Kitchen", subcategory="Small Appliances", image_file="Home&Kitchen/SmallAppliances/BoxGrater.jpg"),
            Product(name="Stainless Steel Toaster", description="Premium 4-slice stainless steel toaster.", price=45 * 80.0, stock=30, category="Home & Kitchen", subcategory="Small Appliances", image_file="Home&Kitchen/SmallAppliances/Stainless.jpg"),
            Product(name="Stoneware Electric Kettle", description="Aesthetic stoneware-style electric kettle.", price=65 * 80.0, stock=25, category="Home & Kitchen", subcategory="Small Appliances", image_file="Home&Kitchen/SmallAppliances/Stoneware.jpg"),
            Product(name="Mini Food Processor", description="Compact chopper for fast food prep.", price=35 * 80.0, stock=35, category="Home & Kitchen", subcategory="Small Appliances", image_file="Home&Kitchen/SmallAppliances/homeaap2.jpg"),
            Product(name="Digital Air Fryer", description="Healthy frying with less oil.", price=99 * 80.0, stock=15, category="Home & Kitchen", subcategory="Small Appliances", image_file="Home&Kitchen/SmallAppliances/homeapp1.jpg"),
            Product(name="Automatic Coffee Maker", description="Programmable drip coffee machine.", price=75 * 80.0, stock=20, category="Home & Kitchen", subcategory="Small Appliances", image_file="Home&Kitchen/SmallAppliances/homeapp3.jpg"),
            Product(name="Personal Blender", description="Great for single-serve smoothies.", price=29 * 80.0, stock=40, category="Home & Kitchen", subcategory="Small Appliances", image_file="Home&Kitchen/SmallAppliances/homeapp4.jpg"),
            Product(name="Stand Mixer", description="Heavy-duty mixer for perfect baking.", price=199 * 80.0, stock=5, category="Home & Kitchen", subcategory="Small Appliances", image_file="Home&Kitchen/SmallAppliances/homeapp5.jpg"),
            Product(name="Slow Cooker", description="Programmable slow cooker for hearty meals.", price=55 * 80.0, stock=12, category="Home & Kitchen", subcategory="Small Appliances", image_file="Home&Kitchen/SmallAppliances/homeapp6.jpg"),
            Product(name="Electric Sandwich Maker", description="Quickly grill and press perfect sandwiches.", price=25 * 80.0, stock=30, category="Home & Kitchen", subcategory="Small Appliances", image_file="Home&Kitchen/SmallAppliances/homeapp7.jpg"),

            # --- HEALTH & FITNESS: Gym Equipment ---
            Product(name="Multi-Purpose Home Gym Station", description="Complete home gym station with high-pulley, leg developer, and chest press.", price=450 * 80.0, stock=5, category="Health & Fitness", subcategory="Gym Equipment", image_file="Fitness/ZymEquipments/equip1.jpg"),
            Product(name="Heavy-Duty Power Rack", description="Professional-grade power rack for safe squats, bench press, and pull-ups.", price=350 * 80.0, stock=8, category="Health & Fitness", subcategory="Gym Equipment", image_file="Fitness/ZymEquipments/equip2.jpg"),
            Product(name="Commercial Olympic Bench", description="Sturdy and adjustable bench for intensive strength training sessions.", price=250 * 80.0, stock=10, category="Health & Fitness", subcategory="Gym Equipment", image_file="Fitness/ZymEquipments/equip3.jpg"),
            Product(name="Cast Iron Kettlebell (16kg)", description="Classic cast iron kettlebell for functional strength and endurance training.", price=45 * 80.0, stock=20, category="Health & Fitness", subcategory="Gym Equipment", image_file="Fitness/ZymEquipments/Kettlebell.jpg"),
            Product(name="Heavy Punching Bag (4ft)", description="High-quality synthetic leather punching bag for boxing and MMA training.", price=95 * 80.0, stock=15, category="Health & Fitness", subcategory="Gym Equipment", image_file="Fitness/ZymEquipments/PunchingBag.jpg"),
            Product(name="Home Pull-Up & Dip Bar", description="Wall-mounted upper body workstation for pull-ups, chin-ups, and dips.", price=65 * 80.0, stock=25, category="Health & Fitness", subcategory="Gym Equipment", image_file="Fitness/ZymEquipments/workoutupper.jpg"),
            Product(name="Adjustable Wrist Strengthener", description="Tension-adjustable forearm and wrist strengthener for better grip power.", price=15 * 80.0, stock=50, category="Health & Fitness", subcategory="Gym Equipment", image_file="Fitness/ZymEquipments/wristequipment.jpg"),
            Product(name="Neoprene Wrist Protector (Pair)", description="Comfortable and supportive wrist wraps for heavy lifting and protection.", price=12 * 80.0, stock=100, category="Health & Fitness", subcategory="Gym Equipment", image_file="Fitness/ZymEquipments/wristprotector.jpg"),

            # --- HEALTH & FITNESS: Cardio Equipment ---
            Product(name="Foldable Electric Treadmill", description="High-performance foldable treadmill with heart rate monitor and auto-incline.", price=550 * 80.0, stock=10, category="Health & Fitness", subcategory="Cardio Equipment", image_file="Fitness/CardioEquipments/cardio1.jpg"),
            Product(name="Magnetic Resistance Exercise Bike", description="Silent magnetic resistance cycling bike for effective home cardio workouts.", price=299 * 80.0, stock=12, category="Health & Fitness", subcategory="Cardio Equipment", image_file="Fitness/CardioEquipments/cadio2.jpg"),
            Product(name="Professional Elliptical Trainer", description="Full-body low-impact cardio trainer with digital display and tracking.", price=399 * 80.0, stock=8, category="Health & Fitness", subcategory="Cardio Equipment", image_file="Fitness/CardioEquipments/cardio3.jpg"),
            Product(name="Adjustable Fluid Rower", description="Water resistance rowing machine for a realistic outdoor rowing experience.", price=499 * 80.0, stock=5, category="Health & Fitness", subcategory="Cardio Equipment", image_file="Fitness/CardioEquipments/cardio4.jpg"),
            Product(name="Compact Multi-Stepper", description="Space-saving stair climber for toning legs and improving cardiovascular health.", price=85 * 80.0, stock=20, category="Health & Fitness", subcategory="Cardio Equipment", image_file="Fitness/CardioEquipments/cardio5.jpg"),
            Product(name="Vertical Climber Machine", description="Full-body vertical climbing machine for high-intensity calorie burning.", price=180 * 80.0, stock=15, category="Health & Fitness", subcategory="Cardio Equipment", image_file="Fitness/CardioEquipments/cardio6.jpg"),

            # --- HEALTH & FITNESS: Yoga & Meditation ---
            Product(name="Premium TPE Yoga Mat (Purple)", description="Non-slip, eco-friendly TPE mat with high density and excellent cushioning.", price=35 * 80.0, stock=40, category="Health & Fitness", subcategory="Yoga & Meditation", image_file="Fitness/YogaMeditation/yogamat1.jpg"),
            Product(name="Eco-Friendly Cork Yoga Mat", description="Sustainable natural cork surface with superior grip even during sweat.", price=55 * 80.0, stock=30, category="Health & Fitness", subcategory="Yoga & Meditation", image_file="Fitness/YogaMeditation/yogamat2.jpg"),
            Product(name="Alignment Print Yoga Mat", description="Professional yoga mat with body alignment lines for perfect posture.", price=45 * 80.0, stock=35, category="Health & Fitness", subcategory="Yoga & Meditation", image_file="Fitness/YogaMeditation/yogamat3.jpg"),
            Product(name="Extra Thick Comfort Mat", description="15mm thick cushioned mat for joint support during yoga and pilates.", price=48 * 80.0, stock=25, category="Health & Fitness", subcategory="Yoga & Meditation", image_file="Fitness/YogaMeditation/yogamat4.jpg"),
            Product(name="Reversible Yoga & Fitness Mat", description="Dual-textured reversible mat for versatile training on different surfaces.", price=42 * 80.0, stock=30, category="Health & Fitness", subcategory="Yoga & Meditation", image_file="Fitness/YogaMeditation/yogamat5.jpg"),

            # --- HEALTH & FITNESS: Supplements ---
            Product(name="Pure Whey Protein Isolate (2kg)", description="Ultrapure 100% whey protein isolate for rapid muscle recovery and growth.", price=65 * 80.0, stock=50, category="Health & Fitness", subcategory="Supplements", image_file="Fitness/Supplements/whey.jpg"),
            Product(name="Performance Mass Tech Gainer", description="Scientifically engineered mass gainer for increased strength and size.", price=55 * 80.0, stock=40, category="Health & Fitness", subcategory="Supplements", image_file="Fitness/Supplements/masstech.jpg"),
            Product(name="Intense Pre-Workout Formula", description="High-energy pre-workout blend for explosive power and focus.", price=35 * 80.0, stock=60, category="Health & Fitness", subcategory="Supplements", image_file="Fitness/Supplements/preworkout.jpg"),
            Product(name="Essential Amino Energy Infusion", description="Refreshing amino acid blend for sustained energy and muscle support.", price=29 * 80.0, stock=75, category="Health & Fitness", subcategory="Supplements", image_file="Fitness/Supplements/amonoenergy.jpg"),
            Product(name="Rapid Energy Performance Gel", description="Quick-absorbing energy gel for endurance during long training sessions.", price=18 * 80.0, stock=100, category="Health & Fitness", subcategory="Supplements", image_file="Fitness/Supplements/energy"),

            # --- HEALTH & FITNESS: Fitness Accessories ---
            Product(name="Adjustable Speed Jump Rope", description="Lightweight, adjustable PVC cable jump rope for high-intensity cardio.", price=12 * 80.0, stock=80, category="Health & Fitness", subcategory="Fitness Accessories", image_file="Fitness/FitnessAccessories/accessories1.jpg"),
            Product(name="Resistance Band Set (5 Levels)", description="Set of 5 premium latex resistance loops for full-body strength training.", price=25 * 80.0, stock=60, category="Health & Fitness", subcategory="Fitness Accessories", image_file="Fitness/FitnessAccessories/access2.jpg"),
            Product(name="Deep Tissue Foam Roller", description="High-density foam roller for muscle recovery and myofascial release.", price=20 * 80.0, stock=45, category="Health & Fitness", subcategory="Fitness Accessories", image_file="Fitness/FitnessAccessories/access3.jpg"),
            Product(name="Gym Gloves with Wrist Support", description="Breathable workout gloves with integrated wraps for maximum grip and safety.", price=18 * 80.0, stock=70, category="Health & Fitness", subcategory="Fitness Accessories", image_file="Fitness/FitnessAccessories/access4.jpg"),
            Product(name="Premium Anti-Slip Gym Chalk", description="Superior moisture-absorbing gym chalk for deadlifts and climbing.", price=10 * 80.0, stock=120, category="Health & Fitness", subcategory="Fitness Accessories", image_file="Fitness/FitnessAccessories/antislip.jpg"),
            Product(name="Elite Performance Training Shoes", description="Multi-functional athletic shoes designed for stability and agility.", price=89 * 80.0, stock=30, category="Health & Fitness", subcategory="Fitness Accessories", image_file="Fitness/FitnessAccessories/atheleticshoes.jpg"),
            Product(name="Genuine Leather Powerlifting Belt", description="Durable 4-inch wide leather belt for maximum core stability during lifts.", price=45 * 80.0, stock=25, category="Health & Fitness", subcategory="Fitness Accessories", image_file="Fitness/FitnessAccessories/powerlifting.jpg"),
            Product(name="Heavy Duty Weighted Dip Belt", description="Contoured weightlifting belt for adding extra resistance to dips and pull-ups.", price=29 * 80.0, stock=20, category="Health & Fitness", subcategory="Fitness Accessories", image_file="Fitness/FitnessAccessories/twobelt.jpg"),

            # --- KIDS: Baby Care ---
            Product(name="Luxury Baby Stroller (Black)", description="Ergonomic all-terrain baby stroller with adjustable reclining seat.", price=199 * 80.0, stock=10, category="Kids", subcategory="Baby Care", image_file="Kids&Toys/BabyCar/car1.jpg"),
            Product(name="Jogger Travel System Plus", description="Versatile jogger stroller with integrated handle and smooth wheels.", price=249 * 80.0, stock=8, category="Kids", subcategory="Baby Care", image_file="Kids&Toys/BabyCar/car2.jpg"),
            Product(name="Urban Umbrella Stroller", description="Lightweight and compact folding stroller for city travel.", price=120 * 80.0, stock=15, category="Kids", subcategory="Baby Care", image_file="Kids&Toys/BabyCar/car3.jpg"),
            Product(name="Twin Seater Baby Pram", description="Spacious and safe double-seat stroller for twins or siblings.", price=349 * 80.0, stock=5, category="Kids", subcategory="Baby Care", image_file="Kids&Toys/BabyCar/car4.jpg"),
            Product(name="Classic Retro Baby Carriage", description="Elegant vintage-inspired baby carriage with soft suspension.", price=399 * 80.0, stock=3, category="Kids", subcategory="Baby Care", image_file="Kids&Toys/BabyCar/car5.jpg"),

            # --- KIDS: Educational Toys ---
            Product(name="Interactive Kids Learning Tablet", description="Educational tablet with pre-loaded games for math, language, and logic.", price=85 * 80.0, stock=25, category="Kids", subcategory="Educational Toys", image_file="Kids&Toys/EducationalToys/edu1.jpg"),
            Product(name="STEM Advanced Solar Robot Kit", description="Solar-powered 14-in-1 robot building set to inspire young engineers.", price=45 * 80.0, stock=30, category="Kids", subcategory="Educational Toys", image_file="Kids&Toys/EducationalToys/edu2.jpg"),
            Product(name="Wooden Spelling & Math Blocks", description="Traditional wooden blocks for developing early literacy and numeracy skills.", price=25 * 80.0, stock=50, category="Kids", subcategory="Educational Toys", image_file="Kids&Toys/EducationalToys/edu3.jpg"),
            Product(name="Magnetic Building Tiles (100pcs)", description="Versatile 3D magnetic tiles for creative construction and spatial learning.", price=65 * 80.0, stock=20, category="Kids", subcategory="Educational Toys", image_file="Kids&Toys/EducationalToys/edu4.jpg"),
            Product(name="Beginner's Electronic Microscope", description="High-resolution digital microscope for exploring the wonders of science.", price=55 * 80.0, stock=15, category="Kids", subcategory="Educational Toys", image_file="Kids&Toys/EducationalToys/edu5.jpg"),

            # --- KIDS: Action & Remote Toys ---
            Product(name="4WD High-Speed Monster Truck", description="Off-road 1:12 scale remote control truck with shock absorbers.", price=99 * 80.0, stock=12, category="Kids", subcategory="Action & Remote Toys", image_file="Kids&Toys/Action&RemoteToys/toy1.jpg"),
            Product(name="RC Stunt Drone with Camera", description="Agile remote control drone capable of 360-degree flips and 720p video.", price=120 * 80.0, stock=10, category="Kids", subcategory="Action & Remote Toys", image_file="Kids&Toys/Action&RemoteToys/toy2.jpg"),
            Product(name="Transformable Fighting Robot", description="Voice-controlled RC robot that transforms into a sleek racing car.", price=75 * 80.0, stock=18, category="Kids", subcategory="Action & Remote Toys", image_file="Kids&Toys/Action&RemoteToys/toy3.jpg"),
            Product(name="Electronic Smart Race Track", description="Gravity-defying race track set with two high-speed LED cars.", price=55 * 80.0, stock=25, category="Kids", subcategory="Action & Remote Toys", image_file="Kids&Toys/Action&RemoteToys/toy4.jpg"),
            Product(name="Intergalactic Battle Figure Set", description="Detailed set of 5 action figures with interchangeable accessories.", price=35 * 80.0, stock=40, category="Kids", subcategory="Action & Remote Toys", image_file="Kids&Toys/Action&RemoteToys/toy5.jpg"),

            # --- KIDS: Board Games ---
            Product(name="Ultimate Family Adventure Game", description="Large board adventure game for 2-6 players, perfect for family nights.", price=45 * 80.0, stock=20, category="Kids", subcategory="Board Games", image_file="Kids&Toys/BoardGame/boar1.jpg"),
            Product(name="Strategical Chess & Checkers Set", description="Foldable wooden board with handcrafted pieces for classic strategy play.", price=25 * 80.0, stock=35, category="Kids", subcategory="Board Games", image_file="Kids&Toys/BoardGame/board2.jpg"),
            Product(name="Mystery Solving Detective Game", description="Cooperative board game where players solve crimes using clues.", price=32 * 80.0, stock=15, category="Kids", subcategory="Board Games", image_file="Kids&Toys/BoardGame/board3.jpg"),
            Product(name="Creative Card Matching Set", description="Fun and fast-paced card matching game for memory improvement.", price=15 * 80.0, stock=50, category="Kids", subcategory="Board Games", image_file="Kids&Toys/BoardGame/board4.jpg"),

            # --- KIDS: School Supplies ---
            Product(name="Ergonomic Orthopedic Backpack", description="Spinal-support backpack with multiple compartments and reflective strips.", price=65 * 80.0, stock=30, category="Kids", subcategory="School Supplies", image_file="Kids&Toys/School supplies/suup1.jpg"),
            Product(name="Hardcase Stationery Organizer", description="Durable hard-shell pencil case with secure elastic pen holders.", price=18 * 80.0, stock=100, category="Kids", subcategory="School Supplies", image_file="Kids&Toys/School supplies/suup2.jpg"),
            Product(name="Artist's Multi-Pocket Portfolio", description="Spacious case for art supplies and large-format sketchbooks.", price=29 * 80.0, stock=40, category="Kids", subcategory="School Supplies", image_file="Kids&Toys/School supplies/suup3.jpg"),
            Product(name="Precision Geometry Compass Set", description="Professional-grade geometry toolset in a protective metal case.", price=15 * 80.0, stock=80, category="Kids", subcategory="School Supplies", image_file="Kids&Toys/School supplies/supp4.jpg"),
            Product(name="Quick-Dry Washable Marker Pack", description="Set of 24 vibrant, non-toxic markers that wash off skin and fabric.", price=22 * 80.0, stock=60, category="Kids", subcategory="School Supplies", image_file="Kids&Toys/School supplies/supp5.jpg"),
            Product(name="Premium Spiral Notebook 5-Pack", description="High-quality 200-page spiral notebooks with tear-resistant covers.", price=25 * 80.0, stock=150, category="Kids", subcategory="School Supplies", image_file="Kids&Toys/School supplies/supp6.jpg"),
            Product(name="Comfort Grip Retractable Pen Set", description="Set of 12 smooth-writing gel pens with non-slip rubber grips.", price=12 * 80.0, stock=200, category="Kids", subcategory="School Supplies", image_file="Kids&Toys/School supplies/supp7.jpg")
        ]

        for p in products:
            db.session.add(p)
        
        db.session.commit()
        print("Global Multi-Category Database Seeded Successfully!")

if __name__ == "__main__":
    seed_data()
