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


from specializations.routes import specializations
from enrollees.routes import enrolees
from faculties.routes import faculties


app.register_blueprint(specializations, url_prefix='/specs')
app.register_blueprint(faculties, url_prefix='/faculties')
app.register_blueprint(enrolees, url_prefix='/enrolees')