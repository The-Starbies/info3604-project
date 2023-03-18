import os
from flask import Flask, Blueprint, render_template,url_for, redirect, request, flash, make_response, jsonify
from flask_login import LoginManager, current_user, login_user, login_required, logout_user
from flask_uploads import DOCUMENTS, IMAGES, TEXT, UploadSet, configure_uploads
from flask_cors import CORS
from werkzeug.utils import secure_filename
from werkzeug.datastructures import  FileStorage
from datetime import timedelta


from App.database import create_db

from App.controllers import (
    setup_jwt
)

from App.views import (
    user_views,
    index_views,
    student_views,
    review_views
)

# New views must be imported and added to this list

views = [
    user_views,
    index_views,
    student_views,
    review_views
]

def add_views(app, views):
    for view in views:
        app.register_blueprint(view)


def loadConfig(app, config):
    app.config['ENV'] = os.environ.get('ENV', 'DEVELOPMENT')
    delta = 7
    if app.config['ENV'] == "DEVELOPMENT":
        app.config.from_object('App.config')
        delta = app.config['JWT_EXPIRATION_DELTA']
    else:
        app.config['SQLALCHEMY_DATABASE_URI'] = os.environ.get('SQLALCHEMY_DATABASE_URI')
        app.config['SECRET_KEY'] = os.environ.get('SECRET_KEY')
        app.config['DEBUG'] = os.environ.get('ENV').upper() != 'PRODUCTION'
        app.config['ENV'] = os.environ.get('ENV')
        delta = os.environ.get('JWT_EXPIRATION_DELTA', 7)
        
    app.config['JWT_EXPIRATION_DELTA'] = timedelta(days=int(delta))
        
    for key, value in config.items():
        app.config[key] = config[key]

def create_app(config={}):
  app = Flask(__name__, static_url_path='/static')
  CORS(app)
  loadConfig(app, config)
  app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
  app.config['TEMPLATES_AUTO_RELOAD'] = True
  app.config['PREFERRED_URL_SCHEME'] = 'https'
  app.config['UPLOADED_PHOTOS_DEST'] = "App/uploads"
  photos = UploadSet('photos', TEXT + DOCUMENTS + IMAGES)
  configure_uploads(app, photos)
  add_views(app, views)
  create_db(app)
  setup_jwt(app)
  app.app_context().push()
  return app

app = create_app()

#Login routes
@app.route("/", methods=['GET'])
def login():
  return render_template('login.html')

@app.route("/login", methods=['POST'])
def login_action():
  data = request.form
  user = User.query.filter_by(username=data['username']).first()
  if user and user.check_password(data['password']):
    flash('Login successful')
    login_user(user)
    return redirect('/app')
  else: 
    flash('Invalid username or password')
  return redirect('/app')

@app.rotue("/", methods =  ['GET'])
def FAQ()
  return render_template('FAQ')