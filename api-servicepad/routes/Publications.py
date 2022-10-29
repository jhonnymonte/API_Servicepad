from config.settings import app, db
from flasgger import swag_from
from models.publications.models import Publication
from flask import request, jsonify
import datetime

from utils.token import token_required



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