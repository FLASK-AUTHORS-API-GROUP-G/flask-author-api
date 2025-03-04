# storing all functions used for performing the different authentication process of log in and log out.
from flask import Blueprint, request, jsonify
from app.status_codes import HTTP_400_BAD_REQUEST, HTTP_409_CONFLICT, HTTP_201_CREATED, HTTP_500_INTERNAL_SERVER_ERROR
import validators 
from app.models.authors import Author
from app.extensions import db, bcrypt



auth = Blueprint('auth', __name__, url_prefix ='api/v1/auth')


# Author registration 

@auth.route('/register', methods = ['POST'])
def register_author():
    data = request.json
    first_name = data.get('first_name')
    last_name = data.get('last_name')
    contact = data.get('contact')
    email = data.get('email')
    type = data.get('type')
    password = data.get('password')
    bio = data.get('bio', '')if type == 'author' else ''
    
    
    #Validation of the incoming request 
    if not first_name or not last_name or not contact or not password or not email:
        return jsonify({"error":"All fields are required"}), HTTP_400_BAD_REQUEST
    
    if type == "author" and not bio:
        return jsonify({"error": "Enter your author biography"}), HTTP_400_BAD_REQUEST
    
    if len(password) < 8:
        return jsonify({"error": "Password is too short. Enter atleast 8 characters"})
    
    if not validators.email(email):
        return jsonify({"error": "Enter a valid email"}), HTTP_400_BAD_REQUEST
    
    if Author.query.filter_by(email=email).first() is not None:
        return jsonify({"error": "This email address is already in use, please select another"}), HTTP_409_CONFLICT
    
    if Author.query.filter_by(contact=contact).first() is not None:
        return jsonify ({"error": "This contact is already in use, Please use another contact."}), HTTP_409_CONFLICT
    
    try:
        hashed_password = bcrypt.generate_password_hash(password) #hashing the password
        
        #creating a new user
        new_author = Author(first_name,last_name,password=hashed_password,email=email,contact=contact,bio = bio,type=type)
        db.session.add(new_author)
        db.session.commit()
        
        #keeping track of the author name
        author_name =new_author.author_info()
        
        return jsonify({
            'message': author_name + 'has been successfully craeted as an' + new_author.type,
            'user':{
                'first_name':new_author.first_name,
                'last_name':new_author.last_name,
                'email':new_author.email,
                'contact':new_author.contact,
                'bio':new_author.bio,
                'type':new_author.type,
                'created_at':new_author.created_at,
            }
        }),HTTP_201_CREATED
        
        
    except Exception as e:
        db.session.rollback()
        return jsonify({'error':str(e)}), HTTP_500_INTERNAL_SERVER_ERROR
    
    