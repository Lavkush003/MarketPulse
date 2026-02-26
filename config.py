import os

class Config:
    SECRET_KEY = os.environ.get('SECRET_KEY') or 'premium-organic-secret-key-123'
    # Use PostgreSQL if DATABASE_URL is set; otherwise fallback to SQLite for local development
    SQLALCHEMY_DATABASE_URI = os.getenv('DATABASE_URL') or 'sqlite:///organic_shop.db'
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    UPLOAD_FOLDER = os.path.join(os.path.abspath(os.path.dirname(__file__)), 'static/uploads')
    MAX_CONTENT_LENGTH = 16 * 1024 * 1024  # 16MB max upload
