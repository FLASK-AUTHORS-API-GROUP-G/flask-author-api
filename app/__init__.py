# Application factory function(Define the app instance within the function) helps to rellate with different 3rd party libraries
from flask import Flask
from app.extensions import db,migrate,jwt
from app.controllers.auth.auth_controller import auth

def create_app():
    
    app = Flask(__name__) 
    app.config.from_object('config.Config')   
    db.init_app(app)   
    migrate.init_app(app,db)    
    jwt.init_app(app)
   
    
    
    # importing and registering models
    from app.models.author_model import Author
    from app.models.company_model import Company
    from app.models.books_model import Book
    
    
    #registering blue prints
    app.register_blueprint(auth)
    
    
    @app.route('/')
    def home():
        return 'Authors API for many times'
    
    
    return app  