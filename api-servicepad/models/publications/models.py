from config.settings import db


class Publication(db.Model): 
    """
    Creation of the models for the publication table
    """ 
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(50), unique=True, nullable=False)   
    description = db.Column(db.Text ) 
    priority = db.Column(db.String(50))  
    status = db.Column(db.Boolean)
    user_id = db.Column(db.Integer)
    created_at = db.Column(db.DateTime, nullable=True)
    updated_at = db.Column(db.DateTime, nullable=True)


    def get_publication(id):
        return [Publication.json(Publication.query.filter_by(id=id).first())]
