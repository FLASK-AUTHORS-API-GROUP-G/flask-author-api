from app.extensions import db
from datetime import datetime

class Author (db.Model):      # inherit from the model class
     __tablename__ = "authors"
     id = db.Column(db.Integer, primary_key=True, nullable = False)
     first_name = db.Column(db.String(20))
     last_name = db.Column(db.String(20))
     contact = db.Column(db.Integer, nullable = False, unique = True)
     email = db.Column(db.String(30), nullable = False, unique = True)
     password = db.Column(db.String(15), nullable = False)
     image = db.Column(db.String(100)) 
     bio = db.Column(db.String(200))
     type = db.Column(db.String(255), nullable = False )
     created_at = db.Column(db.String(50))
     time_stamp = db.Column(db.DateTime, default= datetime.now())
     updated_at = db.Column(db.DateTime, onupdate = datetime.now())
     
     def __init__ (self, first_name, last_name, contact, email, password, image, bio, created_at, time_stamp, updated_at):
          super(Author, self).__init__()
          self.id = id               
          self.first_name = first_name   
          self.last_name = last_name
          self.email = email
          self.password = password           
          self.image= image
          self.bio= bio
          self.created_at= created_at
          self.time_stamp= time_stamp
          self.updated_at= updated_at
          self.contact= contact
        

     def __repr__(self):
       return  f"Author {self.first_name}"