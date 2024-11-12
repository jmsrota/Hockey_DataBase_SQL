import os

class Config:
    SECRET_KEY = os.getenv('SECRET_KEY', '123')
    SQLALCHEMY_DATABASE_URI = os.getenv('DATABASE_URI', 'mysql+pymysql://root:new_password@localhost/hockey_database')
    SQLALCHEMY_TRACK_MODIFICATIONS = False