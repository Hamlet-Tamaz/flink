from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_bcrypt import Bcrypt
from flask_login import LoginManager
from flask_modus import Modus
from flask_marshmallow import Marshmallow
import os

from flask_oauthlib.client import OAuth

import os

app = Flask(__name__)

modus = Modus(app)
bcrypt = Bcrypt(app)


oauth = OAuth(app)
google_id = os.environ.get('GOOGLE_ID')
google_secret = os.environ.get('GOOGLE_SECRET')

from IPython import embed; embed()

app.debug = True
google = oauth.remote_app(
    'google',
    consumer_key=google_id,
    consumer_secret=google_secret,
    request_token_params={
        'scope': 'profile email https://www.googleapis.com/auth/plus.login https://www.googleapis.com/auth/contacts.readonly https://www.googleapis.com/auth/calendar   '
        # profile email calendar contacts.readonly plus.login
    },
    base_url='https://www.googleapis.com/oauth2/v1/',
    request_token_url=None,
    access_token_method='POST',
    access_token_url='https://accounts.google.com/o/oauth2/token',
    authorize_url='https://accounts.google.com/o/oauth2/auth',

    # https://www.googleapis.com/auth
    # https://accounts.google.com/o/oauth2/auth
)

login_manager = LoginManager()
login_manager.init_app(app)
login_manager.login_view = "login"


app.config['SQLALCHEMY_DATABASE_URI'] = os.environ.get('DATABASE_URL') or 'postgres://localhost/flink'

app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db = SQLAlchemy(app)
ma = Marshmallow(app)

from project.users.views import users_blueprint
from project.oauth_google.views import oauthG_blueprint
from project.api.views import api_blueprint
app.register_blueprint(users_blueprint)
app.register_blueprint(oauthG_blueprint, url_prefix='/google')
app.register_blueprint(api_blueprint, url_prefix='/api')


from project.users.models import User, GoogleUser

@login_manager.user_loader
def load_user(id):
    return GoogleUser.query.get(id)