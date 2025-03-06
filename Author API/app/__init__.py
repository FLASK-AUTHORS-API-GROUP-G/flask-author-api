from flask import Flask
from app.extensions import db, migrate, jwt
from app.Controllers.auth.auth_controller import auth

def create_app():
    #Application factory function.
    app = Flask(__name__) #This is an instance, i.e. the variable created.
    app.config.from_object('config.Config') #For applications that have been defined use the config object.
    db.init_app(app)

    #Initializing the migration object within our app location instance.
    migrate.init_app(app, db)
    jwt.init_app(app)
    
    #Migrating(Registering) models***
    from app.Models.author_model import Author
    from app.Models.company_model import Company
    from app.Models.book_model import Book

    #Resgistering blueprints
    app.register_blueprint(auth)

    #Creating an index route
    @app.route('/') 

    def index():
        return "Authors API"

    return app #Returning the app instance.

    #Activating debug mode
app = Flask(__name__)  
app.config['DEBUG'] = True  # Add this line  
