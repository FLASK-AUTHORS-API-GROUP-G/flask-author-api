from flask import Blueprint,request ,jsonify
from app.status_code  import HTTP_400_BAD_REQUEST ,HTTP_409_CONFLICT,HTTP_500_INTERNAL_SERVER_ERROR ,HTTP_201_CREATED 
import validators
from app.models.authors_model import Author
from app.extensions import db , bcrypt




#author blueprints
author = Blueprint('author', __name__,url_prefix='/api/v1/author')

# author registration

@author.route('/register', methods=['POST']) 
def register_user():
    data =request.json

    firstName = data.get('firstName')
    lastName = data.get('last_name')
    contacts = data.get('contacts')
    emailAddress = data.get('emailAddress')
    type = data.get('type') #if 'author_type' in data else 'author'
    password = data.get('password')
    biography = data.get('biography') #if type == 'author' else ''

    if  firstName or  not lastName or not contacts or not password or not emailAddress:
        return  jsonify({"error":"all fields are required"}),HTTP_400_BAD_REQUEST
    
    if type == 'author' and not biography:
        return jsonify({"error": 'Enter your author bioraphy'}),HTTP_400_BAD_REQUEST
    
    if len(password)<8:
        return jsonify({"error": 'password is too short'}),HTTP_400_BAD_REQUEST
    if  not validators.email(emailAddress):
         
         return jsonify({"error": 'email is not valid'}),HTTP_400_BAD_REQUEST

    if Author.query.filter_by(email=emailAddress).first() is not None:
         return jsonify({"error": 'email address in use '}),HTTP_409_CONFLICT
    
    
    if Author.query.filter_by(contact=contacts).first() is not None:
         return jsonify({"error": 'contact is in use'}),HTTP_409_CONFLICT
    
    
    try:
        hashed_password = bcrypt.generate_password_hash(password)#hasing the password
        #creating a new user
        # new_user = Author(first_name=firstName, last_name=lastName , contacts=contacts , emailAddress=emailAddress, biography=biography , password=hashed_password )
        new_user = Author(
        firstName=firstName, 
        lastName=lastName, 
        contacts=contacts, 
        emailAddress=emailAddress, 
        password=hashed_password, 
        biography=biography
    )

        db.session.add(new_user)
        db.session.commit()

        #username
        author = new_user.author_info()

        return jsonify({
            'message': author + "has been successfully created as an anuthor" + new_user.type,
            'Author':{
                "id": new_user.id,
                "firstName":new_user.firstName ,
                "lastName": new_user.lastName,
                "contacts":new_user.contacts,
                "emailAddress":new_user.emailAddress,
                "biography":new_user.biography,
                "created_at": new_user.created_at,
                


            }
        }
            
        ),HTTP_201_CREATED

    except Exception as e:
        db.session.rollback()
        return jsonify({'error':str(e)}),HTTP_500_INTERNAL_SERVER_ERROR
    


