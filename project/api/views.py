from project import google, db
from flask import Flask, redirect, url_for, session, request, jsonify, Blueprint, flash, render_template

from project.users.models import GoogleUser, Message, Friendship, Conversation
from project.users.models import G_UserSchema, ConversationSchema, MessagesSchema

import requests, json

api_blueprint = Blueprint('api', __name__)

G_user_schema = G_UserSchema()
G_users_schema = G_UserSchema(many=True)
Conversation_schema = ConversationSchema(many=True)
Messages_schema = MessagesSchema(many=True)

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
		# 
		return jsonify(result.data)


		# user = GoogleUser.query.get(id)
		# 
		# print (G_user_schema.jsonify(user))
		# return G_user_schema.jsonify(user)

@api_blueprint.route('/users/<id>/google')
def user_info(id):
	if request.headers['Accept'] == 'application/json, text/plain, */*':
		user = GoogleUser.query.filter_by(name = 'Cassandra Brown').first()
		result = G_user_schema.dump(user)

		return jsonify(result.data)



@api_blueprint.route('/users/<id>/edit', methods=['POST'])
def edit_user(id):
	if request.headers['Accept'] == 'application/json, text/plain, */*':
		# decode the JSON from binary
		user = request.data.decode('utf-8')
		# parse the JSON into a dictionary
		parsed_user = json.loads(user)
		# turn the dictionary into a SQL Alchemy model
		user = G_user_schema.load(parsed_user)
		# Save it 
		db.session.add(user.data)
		db.session.commit()
		
		# 
		return jsonify(id)



@api_blueprint.route('/users/<id>/friends/vis')
def user_friends_vis(id):
	if request.headers['Accept'] == 'application/json, text/plain, */*':
		
		user = GoogleUser.query.get(id)
		token = session['google_token'][0]
		headers = {
			'Authorization' : 'Bearer {}'.format(token)
		}

		friends = requests.get('https://www.googleapis.com/plus/v1/people/{me}/people/visible?key=AIzaSyC8x6y_-OeLDHM9Tq232SWXHerihctcgUE'.format(me=user.google_id), headers=headers).content
		
		return friends

@api_blueprint.route('/users/<id>/friends/con')
def user_friends_con(id):
	if request.headers['Accept'] == 'application/json, text/plain, */*':
		
		user = GoogleUser.query.get(id)
		token = session['google_token'][0]
		headers = {
			'Authorization' : 'Bearer {}'.format(token)
		}

		friends = requests.get('https://www.googleapis.com/plus/v1/people/{me}/people/connected?key=AIzaSyC8x6y_-OeLDHM9Tq232SWXHerihctcgUE'.format(me=user.google_id), headers=headers).content
		
		return friends


@api_blueprint.route('/users/<id>/friends/<to_id>')
def user_friend(id, to_id):
	if request.headers['Accept'] == 'application/json, text/plain, */*':

		# user = GoogleUser.query.get(id)
		token = session['google_token'][0]
		headers = {
			'Authorization' : 'Bearer {}'.format(token)
		}

		friend = requests.get('https://www.googleapis.com/plus/v1/people/{}'.format(to_id), headers=headers).content
		
		friend_dec = friend.decode('utf-8')
		friend_dec = json.loads(friend_dec)
		
		# 
		
		if 'error' in friend_dec.keys():
			# 
			return jsonify({})
		else:
			return friend



@api_blueprint.route('/users/<id>/messages/conversations')
def conversations(id):
	if request.headers['Accept'] == 'application/json, text/plain, */*':
		user = GoogleUser.query.get(id)
		# print (G_user_schema.jsonify(user))
		result1 = G_user_schema.dump(user)

		# return jsonify(result.data)

		# conversations = Conversation.query.all()
		conversations = Conversation.query.filter_by( user_id = int(id))
		resultConversations = Conversation_schema.dump(conversations)


		msgdUsersArr = []
		

		for user in resultConversations.data:
			msgdUsersArr.append(user['receiver_id'])

		messagedUsers = GoogleUser.query.filter(GoogleUser.id.in_(msgdUsersArr)).all()


		resultUsers = G_users_schema.dump(messagedUsers)

		# msgdUsersArr = []
		# for user in messagedUsers:
		# 	msgdUsersArr.append(G_user_schema(user))

		# receiver = result.data[1]['receiver_id']


		return jsonify(resultUsers.data)


@api_blueprint.route('/users/<id>/messages/thread/<receiver_id>')
def thread(id, receiver_id):
	if request.headers['Accept'] == 'application/json, text/plain, */*':
		user = GoogleUser.query.get(id)
		receiver = GoogleUser.query.get(receiver_id)
		convArr = [id, receiver_id]


		# messages = Message.query.filter_by(user_id = int(id), receiver_id = int(receiver_id))
		messages = Message.query.filter(GoogleUser.id.in_(convArr))
		result = Messages_schema.dump(messages)


		# 
		return jsonify(result.data)

@api_blueprint.route('/users/<id>/messages/new', methods=['POST'])
def send_message(id):
	if request.headers['Accept'] == 'application/json, text/plain, */*':
		# decode the JSON from binary
		message = request.data.decode('utf-8')
		# parse the JSON into a dictionary
		parsed_message = json.loads(message)
		# turn the dictionary into a SQL Alchemy model
		messageResult = Messages_schema.load(parsed_message)
		# Save it 

		from IPython import embed; embed()
		db.session.add(message.data)
		db.session.commit()

		return jsonify(id)


		# Messages_schema.dump(Message.query.filter_by(receiver_id = 3, **kwargs)

		# messages = Message.query.filter_by(user_id = int(id), receiver_id = receiver)

