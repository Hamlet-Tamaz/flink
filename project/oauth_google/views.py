from flask import Flask, redirect, url_for, session, request, jsonify, Blueprint, flash, render_template
from project.users.models import GoogleUser
from project import google, db
from flask_login import login_user, logout_user, login_required, current_user
from sqlalchemy.exc import IntegrityError

oauthG_blueprint = Blueprint('oauthG', __name__)


@oauthG_blueprint.route('/')
def index():
    if 'google_token' in session:
        me = google.get('userinfo')
        return jsonify({"data": me.data})
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



    try:
        id = int(me.data['id'])
        user = GoogleUser(
            id = me.data['id'],
            name = me.data['name'],
            given_name = me.data['given_name'],
            family_name = me.data['family_name'],
            email = me.data['email'],
            gender = me.data['gender'],
            # google_id = me.data['id'],
            picture = me.data['picture'],
            verified_email = me.data['verified_email']
            )
        db.session.add(user)
        from IPython import embed; embed()
        db.session.commit()

        # id = GoogleUser.query

        # login_user(user)
        flash('Logged in!')
        
        return redirect(url_for('users.home'))
    except IntegrityError:
        error = 'Username already exists'
        return render_template('signup.html', error=error)
    return redirect(url_for('signup.html'))

@google.tokengetter
def get_google_oauth_token():
    return session.get('google_token')


@oauthG_blueprint.route('/logout')
def logout():
    session.pop('google_token', None)
    return redirect(url_for('oauthG.index'))