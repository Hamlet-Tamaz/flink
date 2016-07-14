from project import google, db
from flask import Flask, redirect, url_for, session, request, jsonify, Blueprint, flash, render_template

from project.users.models import GoogleUser
from project.users.models import G_UserSchema



api_blueprint = Blueprint('api', __name__)

G_user_schema = G_UserSchema()
G_users_schema = G_UserSchema(many=True)


@api_blueprint.route('/users')
def users():
	if request.headers['Accept'] == 'application/json, text/plain, */*':
		all_users = GoogleUser.query.all()
		result = G_users_schema.dump(all_users)
		print (all_users)

		return jsonify(result.data)

# print ('json: ', jsonify({"user": user}))
# return jsonify( users.serialize())
# OR
# return user_schema.jsonify(all_users)

@api_blueprint.route('/users/<id>')
def user_detail(id):
	
	if request.headers['Accept'] == 'application/json, text/plain, */*':
		# id = int(id)
		user = GoogleUser.query.get(id)
		print (G_user_schema.jsonify(user))
		result = G_user_schema.dump(user)

		return jsonify(result.data)


		# user = GoogleUser.query.get(id)
		# from IPython import embed; embed()
		# print (G_user_schema.jsonify(user))
		# return G_user_schema.jsonify(user)
