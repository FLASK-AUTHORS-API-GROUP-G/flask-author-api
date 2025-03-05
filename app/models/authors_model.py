


from  datetime import datetime
from app.extensions import db
class Author(db.Model):
      __tablename__ = 'authors'
      id = db.Column( db.Integer, primary_key =True , nullable = False)
      firstName = db. Column(db.String(20),nullable = False)
      lastName = db.Column(db.String(20) , nullable = False)
      password = db.Column(db.String(255), nullable = False)
      contacts = db.Column(db.String(20), nullable = False)
      emailAddress = db. Column (db.String(50) , nullable = False)
      images =db.Column (db.String(255) ,nullable = True)
      type = db.Column(db.String(20), nullable=False)
      biography = db.Column (db.String(150), nullable = False)
      created_at = db.Column(db.DateTime, default = datetime.now)
      updated_at =db.Column(db.DateTime , onupdate = datetime.now)
      

      def __init__(self ,  firstName , lastName , contacts , emailAddress , password, images , biography , created_at, updated_at):
          
          self.firstName = firstName
          self.lastName= lastName
          self.emailAddress = emailAddress
          self.contacts =contacts
          self.password = password
          self.images  =images
          self.biography = biography
          self.created_at =  created_at
          self.updated_at = updated_at
      def author_info(self):
           print(f"{self.firstName}{ self.lastName} ")