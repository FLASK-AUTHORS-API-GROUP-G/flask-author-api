from flask import Blueprint,request, jsonify
from app.status_codes import HTTP_400_BAD_REQUEST, HTTP_409_CONFLICT, HTTP_500_INTERNAL_SERVER_ERROR, HTTP_201_CREATED
import validators
from app.Models.author_model import Author
from app.extensions import db, bcrypt

#auth blueprint
auth=Blueprint('auth', __name__, url_prefix='/api/v1/auth') #leading slash necessary for all urls.

#user registration

@auth.route('/register', methods=['POST'])
def register_user():
    data = request.json #Variable storing incoming requests from the user. json data is the content type.
    first_name = data.get('first_name')
    last_name = data.get('last_name')
    contact = data.get('contact')
    email = data.get('email')
    type = data.get('user_type') if 'user_type' in data else "author"
    password = data.get('password')
    biography = data.get('biography','') if type == "author" else ''

    #Checking for null values/Validation of data
    if not first_name or not last_name or not contact or not password or not email:
        return jsonify({"error":"All fields are required"}), HTTP_400_BAD_REQUEST
    
    #Authors must submit biographies
    if type == 'author' and not biography:
        return jsonify({"error":"Enter your author biography"}), HTTP_400_BAD_REQUEST
    
    #Password has to be 8 characters long
    if len(password) < 8:
        return jsonify({"error":"Password too short"}), HTTP_400_BAD_REQUEST
    
    #Check if email address is valid
    if not validators.email(email):
        return jsonify({"error":"Email is not valid"}), HTTP_400_BAD_REQUEST
    
    #For email addresses already in use
    if Author.query.filter_by(email=email).first() is not None:
        return jsonify({"error":"Email address already in use"}), HTTP_409_CONFLICT
    
    #For contacts to be different
    if Author.query.filter_by(contact=contact).first() is not None:
        return jsonify({"error":"Contact number already in use"}), HTTP_409_CONFLICT
    
    #Logic to store the new user to the database.(Error handling)
    try:
        hashed_password = bcrypt.generate_password_hash(password)
        new_user = Author(first_name=first_name, last_name=last_name, password=hashed_password, email=email, contact=contact, biography=biography, type=type)
        #A third party library bcrypt will be used to hash passwords for enhanced security.
        db.session.add(new_user)
        db.session.commit()
        
        #After creating the user message
        username = new_user.get_full_name()
        return jsonify({
            'message': username +  " has been successfully created as an " + new_user.user_type, 
            'user':{
                "id":new_user.id,
                "first_name":new_user.first_name,
                "last_name":new_user.last_name,
                "email":new_user.email,
                "contact":new_user.contact,
                "type":new_user.user_type,
                "biography":new_user.biography,
                "created_at":new_user.created_at,
            }
        }),HTTP_201_CREATED

    except Exception as e:
        db.session.rollback()
        return jsonify({'error':str(e)}), HTTP_500_INTERNAL_SERVER_ERROR