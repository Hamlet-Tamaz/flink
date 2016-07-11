from flask import Flask, redirect, url_for, session, request, jsonify, Blueprint, flash
# from project import google
import requests
import json
from project.users.models import User


oauthG_blueprint = Blueprint('oauthG', __name__)

@oauthG_blueprint.route('/auth/google', methods=['POST'])
def google():
    access_token_url = 'https://accounts.google.com/o/oauth2/token'
    people_api_url = 'https://www.googleapis.com/plus/v1/people/me/openIdConnect'

    payload = dict(client_id="770134292731-gsjfclovkvfh891kq4nmkgld4pops4au.apps.googleusercontent.com",
                   redirect_uri='http://localhost:3000/oauthG',
                   client_secret="Mpp4U5QtxeO-k2rl6SWbJyC3",
                   code=request.json['code'],
                   grant_type='authorization_code')

    # Step 1. Exchange authorization code for access token.
    r = requests.post(access_token_url, data=payload)
    token = json.loads(r.text)
    headers = {'Authorization': 'Bearer {0}'.format(token['access_token'])}

    # Step 2. Retrieve information about the current user.
    r = requests.get(people_api_url, headers=headers)
    profile = json.loads(r.text)

    # Step 3. (optional) Link accounts.
    if request.headers.get('Authorization'):
        user = User.query.filter_by(google=profile['sub']).first()
        if user:
            response = jsonify(message='There is already a Google account that belongs to you')
            response.status_code = 409
            return response

        payload = parse_token(request)

        user = User.query.filter_by(id=payload['sub']).first()
        if not user:
            response = jsonify(message='User not found')
            response.status_code = 400
            return response
        user.google = profile['sub']
        user.display_name = user.display_name or profile['name']
        db.session.commit()
        token = create_token(user)
        return jsonify(token=token)

    # Step 4. Create a new account or return an existing one.

    user = User.query.filter_by(google=profile['sub']).first()
    if user:
        token = create_token(user)
        return jsonify(token=token)
    u = User(google=profile['sub'],
             display_name=profile['name'])
    db.session.add(u)
    db.session.commit()
    token = create_token(u)
    return jsonify(token=token)


# @oauthG_blueprint.route('/')
# def index():
#     import pdb; pdb.set_trace()
#     access_token = session.get('access_token')
#     if access_token is None:
#         return redirect(url_for('oauthG.login'))

#     access_token = access_token[0]
#     from urllib2 import Request, urlopen, URLError

#     headers = {'Authorization': 'OAuth '+access_token}
#     req = Request('https://www.googleapis.com/oauth2/v1/userinfo',
#                   None, headers)
#     try:
#         res = urlopen(req)
#     except URLError as e:
#         if e.code == 401:
#             # Unauthorized - bad token
#             session.pop('access_token', None)
#             return redirect(url_for('oauthG.login'))
#         return res.read()

#     return res.read()


# @oauthG_blueprint.route('/login')
# def login():
#     callback=url_for('oauthG.authorized', _external=True)
#     import pdb; pdb.set_trace()
#     return google.authorize(callback=callback)



@oauthG_blueprint.route('/')
def logged_in():
    import pdb; pdb.set_trace()
    pass
# # @google.authorized_handler
# def authorized(resp):
#     access_token = resp['access_token']
#     session['access_token'] = access_token, ''
#     return redirect(url_for('oauthG.index'))


# @google.tokengetter
# def get_access_token():
#     return session.get('access_token')


