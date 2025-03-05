#Book class
from app.extensions import db
from datetime import datetime

class Book(db.Model):
        __tablename__ = "books"
        id = db.Column(db.Integer, primary_key = True) 
        title = db.Column(db.String(180),nullable=False)
        pages = db.Column(db.Integer, nullable=False)
        price = db.Column(db.Integer, nullable=False)
        price_unit = db.Column(db.String(50), nullable=False, default='UGX')
        publication_date = db.Column(db.Date, nullable= False)
        isbn = db.Column(db.String(30), nullable=False, unique=True)
        genre = db.Column(db.String(50),nullable=False)
        description = db.Column(db.String(255), nullable = False)
        image = db.Column(db.String(255), nullable=False)
        author_id = db.Column(db.Integer, db.ForeignKey('authors.id'))
        company_id = db.Column(db.Integer, db.ForeignKey('companies.id'))
        author = db.relationship('Author', backref='books')
        company = db.relationship('Company', backref='books')
        created_at = db.Column(db.DateTime,default = datetime.now())
        updated_at = db.Column(db.DateTime,onupdate = datetime.now())
     
        def __init__(self, title, pages, price, price_unit, publication_date, genre, description, isbn=None, image=None):
                super(Book,self).__init__()
                self.title = title
                self.pages = pages
                self.price = price
                self.price_unit = price_unit
                self.publication_date = publication_date
                self.isbn = isbn
                self.genre = genre
                self.description = description
                self.image = image

        def __repr__(self) -> str:
                return f"Book: {self.title}"