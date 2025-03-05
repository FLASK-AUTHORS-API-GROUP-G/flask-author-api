from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from flask_bcrypt import Bcrypt 
from sqlalchemy.sql import func

migrate = Migrate()
db = SQLAlchemy()
bcrypt = Bcrypt()
