from app import app
import os

print(f"DATABASE URI: {app.config['SQLALCHEMY_DATABASE_URI']}")
print(f"INSTANCE PATH: {app.instance_path}")
db_path = os.path.join(app.instance_path, 'organic_shop.db')
print(f"EXPECTED DB PATH: {db_path}")
print(f"DB EXISTS: {os.path.exists(db_path)}")
if os.path.exists(db_path):
    print(f"FILE SIZE: {os.path.getsize(db_path)} bytes")
