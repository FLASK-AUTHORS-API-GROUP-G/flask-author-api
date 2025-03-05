

 
from app.extensions import db

class Book(db.Model):
  __tablename__ ="books"
  id = db.Column( db.Integer, primary_key =True)
  title = db. Column(db.String(150),nullable=False)
  price = db.Column(db.Integer, nullable = False)
  description = db.Column(db.String(255), nullable = False)
  image = db. Column (db.String(255), nullable=False)
  price_unit = db.Column(db.Integer)
  no_of_pages =db.Column (db.Integer)
  publication_date = db.Column (db.String(120))
  Author_id = db.Column(db.Integer,db.ForeignKey('authors.id'))
  Company_id = db.Column(db.Integer,db.ForeignKey("companies.id"))
  Author = db.relationship('Author',backref='books')
  Company = db.relationship('Company',backref='books')


  def __init__(self ,id , title, price , description ,image,no_of_pages ,price_unit , publication_date):
     self.title = title
     self.price = price
     self.description = description
     self.image =image
     self.no_of_pages = no_of_pages
     self.price_unit = price_unit
     self.publication_date = publication_date
  def book_info(self):
           print(f" title{self.title},description{ self.description} ,price{self.price} , no_of_pages{self.no_of_pages}, image{self.image} , publication_date{self.publication_date}")