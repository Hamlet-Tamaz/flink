from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_bcrypt import Bcrypt
from flask_login import LoginManager
from flask_modus import Modus
from flask_marshmallow import Marshmallow


from flask_oauthlib.client import OAuth

app = Flask(__name__)

modus = Modus(app)
bcrypt = Bcrypt(app)


oauth = OAuth(app)
app.config['GOOGLE_ID'] = "770134292731-gsjfclovkvfh891kq4nmkgld4pops4au.apps.googleusercontent.com"
app.config['GOOGLE_SECRET'] = "Mpp4U5QtxeO-k2rl6SWbJyC3"
#  TODO: move secret out


app.debug = True
google = oauth.remote_app(
    'google',
    consumer_key=app.config.get('GOOGLE_ID'),
    consumer_secret=app.config.get('GOOGLE_SECRET'),
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


app.secret_key = 'secrets' # Move me to a .env file!

app.config['SQLALCHEMY_DATABASE_URI'] = 'postgres://localhost/flink'
app.config['SQLALCHEMY_TRIACK_MODIFICATIONS'] = False

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