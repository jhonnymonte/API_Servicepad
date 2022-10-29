from api.auth.models import Users
from config.settings import app, db
from flasgger import swag_from
from flask import request, jsonify, make_response
from werkzeug.security import generate_password_hash, check_password_hash
from werkzeug.utils import secure_filename
from utils.token import token_required
from utils.image_file import allowed_file

import datetime
import jwt
import os
import uuid

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


@app.route('/api/auth', methods=['PUT'])
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
