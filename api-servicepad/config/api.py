from api.auth.models import Users
from api.publications.models import Publication
from config.settings import app, db
from flasgger import swag_from
from flask import request, jsonify, make_response, current_app
from functools import wraps
from werkzeug.security import generate_password_hash, check_password_hash
from werkzeug.utils import secure_filename

import datetime
import jwt
import os
import uuid


UPLOAD_FOLDER = 'static/users/'
ALLOWED_EXTENSIONS = {'png', 'jpg', 'jpeg', 'gif'}
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER

def allowed_file(filename):
    return '.' in filename and \
           filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS


def token_required(info):  
    @wraps(info)  
    def decorator(*args, **kwargs):
        token = None 

        if 'X-Access-Token' in request.headers:  
            token = request.headers['X-Access-Token'] 
        if not token:  
            return jsonify({'message': 'a valid token is missing'})   
        try:  
            data=jwt.decode(token, current_app.config["SECRET_KEY"], algorithms=["HS256"])
            current_user = Users.query.filter_by(public_id=data['public_id']).first()
        except:  
            return jsonify({'message': 'token is invalid'})  


        return info(current_user, *args,  **kwargs)  
    return decorator 

    

@app.route('/api/auth/register', methods=['POST'])
@swag_from('../docs/auth/register.yaml')
def signup_user(): 
    data = request.get_json()  

    hashed_password = generate_password_hash(data['password'], method='sha256')
    
    new_user = Users(
        public_id=str(uuid.uuid4()),
        fullname=data['fullname'], 
        email=data['email'], 
        password=hashed_password, 
        images='', 
    ) 
    db.session.add(new_user)  
    db.session.commit()      

    return jsonify({'message': 'registered successfully'}) 


@app.route('/api/auth/login', methods=['POST']) 
@swag_from('../docs/auth/auth.yaml')
def login_user(): 
    
    auth = request.get_json()

    if not auth or not auth['email'] or not auth['password']:  
        return make_response('could not verify', 401,{' failed Authentication': 'info: "login required"'})    
    user = Users.query.filter_by(email=auth['email']).first()   
     
    if check_password_hash(user.password, auth['password']):  
        token = jwt.encode(
            {
                'public_id': user.public_id, 
                'exp' : datetime.datetime.utcnow() + datetime.timedelta(minutes=30)
            }, 
            app.config['SECRET_KEY']
        )  
        return jsonify({'token' : token}) 

    return make_response('could not verify', 401,{'failed Authentication': 'info: "login required"'})


@app.route('/api/auth', methods=['POST'])
@swag_from('../docs/auth/users/update.yaml')
@token_required
def update_user(current_user):
    request_data = request.form
    user = Users.query.filter_by(id=current_user.id).first()
    file = request.files['images']

    if file.filename == '':
        user.images = ''
    
    elif file and allowed_file(file.filename):
        filename = secure_filename(file.filename)
        file.save(os.path.join(app.config['UPLOAD_FOLDER'], filename))
        user.images = filename


    hashed_password = generate_password_hash(request_data['password'])
    user.fullname = request_data['fullname']
    user.email = request_data['email']
    user.password = hashed_password

    db.session.commit()   
    return jsonify({'message': 'user update'})



@app.route('/api/auth', methods=['GET'])
@swag_from('../docs/auth/users/get_user.yaml')
def get_all_users():  
   
   users = Users.query.all() 
   result = []   

   for user in users:   
       user_info = {}   
       user_info['public_id'] = user.public_id  
       user_info['fullname'] = user.fullname
       user_info['email'] = user.email
       user_info['password'] = user.password
       user_info['images'] = user.images 
       
       result.append(user_info)   

   return jsonify({'users': result})  



@app.route('/api/publications', methods=['GET'])
@swag_from('../docs/publications/get_publications.yaml')
@token_required
def get_publications(current_user):

    publications = Publication.query.filter_by(user_id=current_user.id).all()
    output = []
    for publication in publications:
        publication_info = {}
        publication_info['id'] = publication.id
        publication_info['title'] = publication.title
        publication_info['description'] = publication.description
        publication_info['priority'] = publication.priority
        publication_info['status'] = publication.status
        publication_info['created_at'] = publication.created_at
        publication_info['updated_at'] = publication.updated_at
        output.append(publication_info)

    return jsonify({'list_of_publicatios' : output})


@app.route('/api/publications/<pub_id>', methods=['GET'])
@swag_from('../docs/publications/get_publications_id.yaml')
@token_required
def get_publications_id(self, pub_id):
    output = []
    publication = Publication.query.filter_by(id=pub_id).first()
    publication_info = {}
    publication_info['id'] = publication.id
    publication_info['title'] = publication.title
    publication_info['description'] = publication.description
    publication_info['priority'] = publication.priority
    publication_info['status'] = publication.status
    publication_info['created_at'] = publication.created_at
    publication_info['updated_at'] = publication.updated_at
    output.append(publication_info)
    return jsonify({'publication' : output})


@app.route('/api/publications', methods=['POST'])
@swag_from('../docs/publications/create_publication.yaml')
@token_required
def create_publication(current_user):
    data = request.get_json() 

    new_publication = Publication(
                    title=data['title'], 
                    description=data['description'], 
                    priority=data['priority'], 
                    status=data['status'],
                    created_at=datetime.datetime.utcnow(),
                    user_id=current_user.id
    )  
    db.session.add(new_publication)   
    db.session.commit()   

    return jsonify({'message' : 'new publication created'})


@app.route('/api/publications/<pub_id>', methods=['DELETE'])
@swag_from('../docs/publications/delete_publication.yaml')
@token_required
def delete_publication(current_user, pub_id):
    publication = Publication.query.filter_by(id=pub_id, user_id=current_user.id).first()
    if not publication:   
       return jsonify({'message': 'publication does not exist'})   

    db.session.delete(publication)  
    db.session.commit()   

    return jsonify({'message': 'publication deleted'})


@app.route('/api/publications/<int:id>', methods=['PUT'])
@swag_from('../docs/publications/update_publication.yaml')
@token_required
def update_publication(current_user, id):
    request_data = request.get_json()
    publication = Publication.query.filter_by(id=id, user_id=current_user.id).first()
    if not publication:   
       return jsonify({'message': 'publication does not exist'})   

    publication.title = request_data['title']
    publication.year = request_data['description']
    publication.priority = request_data['priority']
    publication.status = request_data['status']
    publication.updated_at = datetime.datetime.utcnow()
    
    db.session.commit()   

    return jsonify({'message': 'publication update'})