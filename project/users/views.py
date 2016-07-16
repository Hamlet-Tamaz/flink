from flask import flash, redirect, url_for, render_template, request, Blueprint, jsonify, session
from project.users.forms import SignupForm, LoginForm
from project.users.models import User, GoogleUser, Friendship, Message
from project import db, bcrypt
from flask_login import login_user, logout_user, login_required, current_user
from sqlalchemy.exc import IntegrityError
from functools import wraps

import requests


users_blueprint = Blueprint('users', __name__, template_folder='templates', static_folder='static', static_url_path='/static/js')
# StackOverflow post for static_url_path http://stackoverflow.com/questions/22152840/flask-blueprint-static-directory-does-not-work
def prevent_login_signup():
    def wrapper(f):
        @wraps(f)
        def wrapped(*args, **kwargs):
            if current_user.is_authenticated:
                flash("You are already logged in")
                return redirect(url_for('users.home'))
            return f(*args, **kwargs)
        return wrapped
    return wrapper

@users_blueprint.route('/',)
@users_blueprint.route('/home',)
def home():
    # from IPython import embed; embed()
    return render_template('home.html')



@users_blueprint.route('/users/<id>/dash')
# users/<id>
# @login_required

#       HOW TO SEND IN THE ID FROM WHERE THIS LINK COMES?
#  FOR EXAMPLE FROM THE LOGIN PAGE
def dash(id):
    user = GoogleUser.query.get_or_404(id)
    name = 'hamlet'
    # if request.headers['Accept'] == 'application/json, text/plain, */*':
    #     from IPython import embed; embed()
    #     print (user)
    #     # print ('json: ', jsonify({"user": user}))
    #     return jsonify( user.serialize())

    return render_template('dash.html', user = user)




@users_blueprint.route('/signup', methods=["GET", "POST"])
@prevent_login_signup()
def signup():
    error = None
    form = SignupForm(request.form)
    if request.method == 'POST':
        # from IPython import embed; embed()
        if form.validate_on_submit():
            user = User(
                name=request.form['name'],
                password=request.form['password']
                )
            try:
                db.session.add(user)
                db.session.commit()
                login_user(user)
                flash('Logged in!')
                return redirect(url_for('users.dash', id = user.id))
            except IntegrityError:
                error = 'Username already exists'
                return render_template('signup.html', form=form, error=error)
        else:
            return render_template('signup.html', form=form, error=error)
    else:
        return render_template('signup.html', form=form, error=error)

@users_blueprint.route('/login', methods=["GET", "POST"])
# @prevent_login_signup()
def login():
    error = None
    form = LoginForm(request.form)
    # from IPython import embed; embed()
    if request.method == 'POST':
        # from IPython import embed; embed()  
        if form.validate_on_submit():
            user = User.query.filter_by(name=request.form['name']).first()
            if user is not None and bcrypt.check_password_hash(user.password, form.password.data ):
                login_user(user)
                flash('Logged in!')
                return redirect(url_for('users.dash', id = user.id))
            else:
                error = "Invalid Credentials, please try again."
                return render_template('login.html',form=form,error=error)
        else:
            return render_template('login.html',form=form,error=error)
    # from IPython import embed; embed()
    return render_template('login.html',form=form,error=error)


@users_blueprint.route('/users/<id>/setup')
def setup(id):
    user = GoogleUser.query.get(id)
    from IPython import embed; embed()

    return render_template('setup.html', user = user)


@users_blueprint.route('/users/<id>/edit')
def edit(id):
    user = GoogleUser.query.get(id)

    from IPython import embed; embed()
    return render_template('edit.html', user = user)


@users_blueprint.route('/users/<id>/update', methods=['POST'])
def update(id):
    user = GoogleUser.query.get(id)

    from IPython import embed; embed()
    
    user.given_name = request.form





@users_blueprint.route('/users/<id>/friends')
# @login_required
def friends(id):
    user = GoogleUser.query.get(id)

    token = session['google_token'][0]
    headers = {
        'Authorization' : 'Bearer {}'.format(token)
    }

    from IPython import embed; embed()

    friends = requests.get('https://www.googleapis.com/plus/v1/people/{}/people/visible?key=AIzaSyC8x6y_-OeLDHM9Tq232SWXHerihctcgUE'.format(user.google_id), headers=headers).content
    

    # from IPython import embed; embed()

    return render_template('friends.html', user = user, friends = friends)


@users_blueprint.route('/users/<id>/calendar')
# @login_required
def calendar(id):
    user = GoogleUser.query.get(id)
    return render_template('calendar.html', user=user)

@users_blueprint.route('/users/<id>/messages')
def messages(id):
    user = GoogleUser.query.get(id)
    inbox = Message.query.filter_by(receiver_id = user.id)
    outbox = Message.query.filter_by(sender_id = user.id)

    from IPython import embed; embed()

    return render_template('messages.html', user = user, inbox=inbox, outbox = outbox)

@users_blueprint.route('/users/<id>/messages/new')
def new_message(id):
    user = GoogleUser.query.get(id)
    return render_template('new_message.html', user = user)


@users_blueprint.route('/users/<id>/messages/new/<to_id>')
def new_message_W(id, to_id):

    user = GoogleUser.query.get(id)

    token = session['google_token'][0]
    headers = {
        'Authorization' : 'Bearer {}'.format(token)
    }


    friend = GoogleUser.query.filter_by(google_id=to_id).first() 

    if not friend:
        friend = requests.get('https://www.googleapis.com/plus/v1/people/{}?key=AIzaSyC8x6y_-OeLDHM9Tq232SWXHerihctcgUE'.format(to_id), headers=headers).json()
    
    from IPython import embed; embed()
    return render_template('new_message_W.html', user=user, friend=friend)



@users_blueprint.route('/logout')
# @login_required
def logout():
    logout_user()
    flash('Logged out!')
    return redirect(url_for('users.login'))



