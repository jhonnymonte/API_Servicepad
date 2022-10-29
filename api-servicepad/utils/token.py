from flask import request, jsonify
from functools import wraps
from flask import request, jsonify,current_app
import jwt
from api.auth.models import Users


def token_required(info):  
    @wraps(info)  
    def create_token(*args, **kwargs):
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
    return create_token 