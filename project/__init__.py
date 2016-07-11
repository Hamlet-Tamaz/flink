from flask import Flask
from flask_sqlalchemy import SQLAlchemy 
from flask_bcrypt import Bcrypt 
from flask_login import LoginManager
from flask_modus import Modus

from flask_oauth import OAuth



app = Flask(__name__)
# 
modus = Modus(app)
bcrypt = Bcrypt(app)

oauth = OAuth()
app.config['GOOGLE_ID'] = "770134292731-gsjfclovkvfh891kq4nmkgld4pops4au.apps.googleusercontent.com"
app.config['GOOGLE_SECRET'] = "Mpp4U5QtxeO-k2rl6SWbJyC3"
app.debug = True
google = oauth.remote_app(
    'google',
    consumer_key=app.config.get('GOOGLE_ID'),
    consumer_secret=app.config.get('GOOGLE_SECRET'),
    request_token_params={
        'scope': 'email'
    },
    base_url='https://www.googleapis.com/oauth2/v1/',
    request_token_url=None,
    access_token_method='POST',
    access_token_url='https://accounts.google.com/o/oauth2/token',
    authorize_url='https://accounts.google.com/o/oauth2/auth',
)


login_manager = LoginManager()
login_manager.init_app(app)
login_manager.login_view = "login"


app.secret_key = 'secrets' # Move me to a .env file!

app.config['SQLALCHEMY_DATABASE_URI'] = 'postgres://localhost/flink'
app.config['SQLALCHEMY_TRIACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)


from project.users.views import users_blueprint
from project.oauth_google.views import oauthG_blueprint
app.register_blueprint(users_blueprint)
app.register_blueprint(oauthG_blueprint, url_prefix='/oauthG')


from project.users.models import User

@login_manager.user_loader
def load_user(id):
	return User.query.get(id)