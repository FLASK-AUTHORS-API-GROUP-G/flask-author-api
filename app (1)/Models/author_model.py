#Author class
from app.extensions import db
from datetime import datetime

class Author(db.Model):
        #By default, the table name will be Author.
        __tablename__ = "authors"
        id = db.Column(db.Integer, primary_key=True,nullable=False) 
        first_name = db.Column(db.String(22),nullable=False)
        last_name = db.Column(db.String(22),nullable=False)
        contact = db.Column(db.Integer,nullable=False,unique=True)
        email = db.Column(db.String(22),nullable=False,unique=True)
        password = db.Column(db.String(8),nullable=False)
        biography = db.Column(db.Text(),nullable=False)
        user_type = db.Column(db.String(20),default='author')
        image = db.Column(db.String(255),nullable=True) # Image is nullable because: A link for the image can be uploaded, optionally.
        created_at = db.Column(db.DateTime,default = datetime.now())
        updated_at = db.Column(db.DateTime,onupdate = datetime.now())
     
        def __init__(self,first_name,last_name,contact,email,password,user_type, image=None):
          super(Author,self).__init__()
          self.first_name = first_name
          self.last_name = last_name
          self.contact = contact
          self.email = email
          self.password = password
          self.user_type = user_type
          self.image = image

        def get_full_name(self):
             return f"{self.last_name}{self.first_name}"
     
#         def author_info(self):
#          print (f"The Author's first name is {self.first_name} and last name is {self.last_name}. His ID is {self.id}, contact is {self.contact}, you can email him at {self.email}, image is {self.image} with a password key {self.password}.")


#             # new instance
# authors_book = Author ("Writer","Faith","Apio","+256 775 070 666","faith@gmail.com","111")
# authors_book.author_info()
        
    
