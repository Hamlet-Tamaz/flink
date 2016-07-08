from flask import flash, redirect, url_for, render_template, request, Blueprint
from project.users.forms import SignupForm, LoginForm
from project.users.models import User
from project import db, bcrypt
from flask_login import login_user, logout_user, login_required, current_user
from sqlalchemy.exc import IntegrityError
from functools import wraps


users_blueprint = Blueprint('users', __name__, template_folder='templates', static_folder='/static')

def prevent_login_signup():
    def wrapper(f):
        @wraps(f)
        def wrapped(*args, **kwargs):
            if current_user.is_authenticated:
                flash("You are already logged in")
                return redirect(url_for('users.home', user_id=current_user.id))
            return f(*args, **kwargs)
        return wrapped
    return wrapper



@users_blueprint.route('/')
@login_required
def home():
    return render_template('home.html')




@users_blueprint.route('/signup', methods=["GET", "POST"])
@prevent_login_signup()
def signup():
    error = None
    form = SignupForm(request.form)
    if request.method == 'POST':
        from IPython import embed; embed()
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
                return redirect(url_for('users.home', user_id=user.id))
            except IntegrityError:
                error = 'Username already exists'
                return render_template('signup.html', form=form, error=error)
        else:
            return render_template('signup.html', form=form, error=error)
    else:
        return render_template('signup.html', form=form, error=error)

@users_blueprint.route('/login', methods=["GET", "POST"])
@prevent_login_signup()
def login():
    error = None
    form = LoginForm(request.form)
    if request.method == 'POST':
        if form.validate_on_submit():
            user = User.query.filter_by(name=request.form['name']).first()
            if user is not None and bcrypt.check_password_hash(user.password, form.password.data ):
                login_user(user)
                flash('Logged in!')
                return redirect(url_for('posts.index', user_id=user.id))
            else:
                error = "Invalid Credentials, please try again."
                return render_template('login.html',form=form,error=error)
        else:
            return render_template('login.html',form=form,error=error)
    return render_template('login.html',form=form,error=error)

@users_blueprint.route('/logout')
@login_required
def logout():
    logout_user()
    flash('Logged out!')
    return redirect(url_for('users.login'))