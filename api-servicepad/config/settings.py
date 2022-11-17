from flask import Flask, current_app
from flask_sqlalchemy import SQLAlchemy
from flasgger import Swagger
from flask_marshmallow import Marshmallow
from config.swagger import swagger_config, template


app = Flask(__name__)
ma = Marshmallow(app)

UPLOAD_FOLDER = 'static/users/'
SECRET_KEY = 'JUaZYfFml7'
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER
app.config['SECRET_KEY'] = SECRET_KEY
app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql+psycopg2://postgres:admin@localhost/blog_api_db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False


db = SQLAlchemy(app)
Swagger(app, config=swagger_config, template=template)


