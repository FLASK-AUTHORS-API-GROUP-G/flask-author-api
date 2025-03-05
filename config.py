# creating a class called config
class Config:
    SQLALCHEMY_DATABASE_URI = 'mysql+pymysql://root:@localhost/flask_authors_db'
    JWT_SECRET_KEY = "author"
    
    SQLALCHEMY_DATABASE_URI = "mysql+pymysql://root:@localhost/author_db"