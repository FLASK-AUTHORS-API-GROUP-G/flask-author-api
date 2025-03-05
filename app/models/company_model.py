# class Company :
    # def __init__(self , id,origin , description ,created_at , updated_at):
       # self.id = id
       # self.origin = origin
        #self.desription= description
        #self.created_at = created_at
       # self.updated-at =updated_at


from  datetime import datetime
from app.extensions import db

class Company (db.Model):
    __tablename__ = 'companies'
    id = db.Column( db.Integer, primary_key =True)
    name = db.Column(db.String(100),unique=True , nullable=False)
    origin = db. Column(db.String(100))
    discription = db.Column(db.String(150))
    Author_id = db.Column(db.Integer,db.ForeignKey('authors.id'))
    created_at= db. Column (db.DateTime,default=datetime.now())
    updated_at= db.Column (db.DateTime,onupdate=datetime.now())

class Company :
     def __init__(self , id, name,origin , description ,created_at , updated_at):
        self.id = id
        self.name = name
        self.origin = origin
        self.desription= description
        self.created_at = created_at
        self.updated_at =updated_at
        def author_info(self):
        
           print(f" name{self.name},origin{ self.origin} ,description{self.discription} , created_at{self.created_at}, updated_at{self.updated_at}")
