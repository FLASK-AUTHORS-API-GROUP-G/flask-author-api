from flask import Flask
from app.extensions  import  db , migrate
from app.extensions import db, migrate
from app.extensions import db
from app.controllers.author.auth_controller import author



def create_app(): #creating  application factory function 

    app = Flask(__name__) # its used to define the root application
    #index route since its the first route
    
    app.config.from_object('config.Config') 
    db.init_app(app)
    migrate.init_app(app,db)
    

    #importing and registering the models
    from app.models.authors_model import Author
    from app.models.books_model import Book
    from app.models.company_model import Company 

    # registering blue prints
    app.register_blueprint(author
    )





    @app.route("/")
    def index():
        return 'hello'

    return app  #returning the application instance  an instance is an object from the class

