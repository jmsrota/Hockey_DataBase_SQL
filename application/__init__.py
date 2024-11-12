
from flask import Flask
from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

def create_app():
    app = Flask(__name__)
    app.config.from_object('application.config.Config')
    
    # Initialize SQLAlchemy
    db.init_app(app)

    with app.app_context():
        from . import routes, models  # Import routes and models
        db.create_all()  # Create tables if they don't already exist

    return app