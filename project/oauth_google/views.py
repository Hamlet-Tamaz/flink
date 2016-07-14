from flask import Flask, redirect, url_for, session, request, jsonify, Blueprint, flash, render_template
from project.users.models import GoogleUser
from project.users.forms import SignupForm, LoginForm
from project import google, db
from flask_login import login_user, logout_user, login_required, current_user
from sqlalchemy.exc import IntegrityError

oauthG_blueprint = Blueprint('oauthG', __name__)


@oauthG_blueprint.route('/')
def index():
    if 'google_token' in session:
        me = google.get('userinfo')
        # return jsonify({"data": me.data})
        id = me.data['id']
        return redirect(url_for('users.dash', id = id))

    return redirect(url_for('oauthG.login'))

@oauthG_blueprint.route('/login')
def login():
    return google.authorize(callback=url_for('oauthG.authorized', _external=True))

@oauthG_blueprint.route('/login/authorized')
def authorized():


    resp = google.authorized_response()
    if resp is None:
        return 'Access denied: reason=%s error=%s' % (
            request.args['error_reason'],
            request.args['error_description']
        )
    session['google_token'] = (resp['access_token'], '')
    me = google.get('userinfo')
    # console.log( jsonify({"data": me.data}))

    id = 0

    try:
        user = GoogleUser(
            name = me.data['name'],
            given_name = me.data['given_name'],
            family_name = me.data['family_name'],
            email = me.data['email'],
            gender = me.data['gender'],
            google_id = me.data['id'],
            picture = me.data['picture'],
            verified_email = me.data['verified_email']
            )

        db.session.add(user)
        db.session.commit()
        # login_user(user)
        flash('Logged in!')

        id = user.id
        # how to know what the id is?
        # id = me.data['id']

        return redirect(url_for('users.setup', user = user, id = id))
    except IntegrityError:
        # error = 'Username already exists'
        # form = SignupForm(request.form)
        db.session.rollback()
        user = GoogleUser.query.filter_by(google_id=me.data['id']).first()
        return redirect(url_for('users.dash', user = user, id = user.id))
        # return redirect(url_for('users.signup', form=form, error = error))


@google.tokengetter
def get_google_oauth_token():
    return session.get('google_token')


@oauthG_blueprint.route('/logout')
def logout():
    session.pop('google_token', None)
    # logout_user()
    return redirect(url_for('users.home'))