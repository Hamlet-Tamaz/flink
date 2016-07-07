# from app import app
# from flask import render_template, url_for, request, redirect
# from flask_login import LoginManager, login_user, logout_user, login_required, current_user
# from flask_modus import Modus
# # from models.user import User

# modus = Modus(app)
# bcrypt = Bcrypt(app)
# login_manager = LoginManager()
# login_manager.init_app(app)
# # login_manager.login_view = "login"

# @app.route('/')
# def index():
# 	return render_template('home.html')

# @app.route('/login', methods=['GET', 'POST'])
# def login():
#     # Here we use a class of some kind to represent and validate our
#     # client-side form data. For example, WTForms is a library that will
#     # handle this for us, and we use a custom LoginForm to validate.
#     form = LoginForm()
#     if form.validate_on_submit():
#         # Login and validate the user.
#         # user should be an instance of your `User` class
#         login_user(user)

#         flask.flash('Logged in successfully.')

#         next = flask.request.args.get('next')
#         # next_is_valid should check if the user has valid
#         # permission to access the `next` url
#         if not next_is_valid(next):
#             return flask.abort(400)

#         return redirect(next or url_for('index'))
#     return render_template('login.html', form=form)


# @app.route('/friends')
# # @login_required
# def friends():
# 	return render_template('friends.html')


# @app.route("/logout")
# # @login_required
# def logout():
#     logout_user()
#     return redirect(url_for('login'))


# @login_manager.user_loader
# def load_user(id):
# 	return User.query.get(id)
