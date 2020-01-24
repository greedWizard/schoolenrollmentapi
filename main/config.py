from flask import Flask, request, jsonify
from flask_sqlalchemy import SQLAlchemy
from flask_marshmallow import Marshmallow
from flask_migrate import Migrate
import os


# Init app 
app = Flask(__name__)


# Database init
basedir = os.path.abspath(os.path.dirname(__file__))
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///' + os.path.join(basedir, 'db.sqlite')
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

# Init db
db = SQLAlchemy(app)

# Init ma
ma = Marshmallow(app)

# Init migrations
migrate = Migrate(app, db)


from specialties.routes import specialties
from enrollees.routes import enrollees
from faculties.routes import faculties
from exams.routes import exams


app.register_blueprint(specialties, url_prefix='/specialties')
app.register_blueprint(faculties, url_prefix='/faculties')
app.register_blueprint(enrollees, url_prefix='/enrollees')
app.register_blueprint(exams, url_prefix='/exams')