from app.extensions import db
from datetime import datetime
class Author(db.Model):
    __tablename__ = "authors"
    id = db.Column(db.Integer, primary_key=True)
    first_name = db.Column(db.String(50), nullable=False)
    last_name = db.Column(db.String(100), nullable=False)
    email = db.Column(db.String(100), nullable=False, unique=True)
    contact = db.Column(db.String(50), nullable=False, unique=True)
    image = db.Column(db.String(255), nullable=True) 
    password = db.Column(db.String(255), nullable=False)
    authors_id = db.Column(db.Integer, db.ForeignKey('authors.id'))
    biography = db.Column(db.Text(), nullable=False)
    user_type = db.Column(db.String(100), default='author')
    created_at = db.Column(db.DateTime, default=datetime.now())
    updated_at = db.Column(db.DateTime, default=datetime.now(), onupdate=datetime.now())

    def __init__(self, first_name, last_name, email, contact, password, biography, user_type='author', image=None):
        self.first_name = first_name
        self.last_name = last_name
        self.email = email
        self.contact = contact
        self.password = password
        self.biography = biography
        self.user_type = user_type
        self.image = image  # Optional field

    def get_full_name(self):
        return f"{self.last_name} {self.first_name}"


        
    
