from project import db, bcrypt, ma
from flask_login import UserMixin
from marshmallow import Schema, fields, pprint, post_load

import datetime

class User(db.Model, UserMixin):
	__tablename__ = 'users'

	id = db.Column(db.Integer, primary_key=True)
	name = db.Column(db.Text)
	password = db.Column(db.Text)

	def __init__(self, name, password):
		self.name = name
		self.password = bcrypt.generate_password_hash(password).decode('utf-8')

	def __repr__(self):
		return 'name: {0} - password: {1}'.format(self.name, self.password)

class GoogleUser(db.Model):
	__tablename__ = 'google_users'

	id = db.Column(db.Integer, primary_key=True)
	google_id = db.Column(db.Text, unique=True)
	name = db.Column(db.Text)
	title = db.Column(db.Text)
	given_name = db.Column(db.Text)
	family_name = db.Column(db.Text)
	gender = db.Column(db.Text)
	dob = db.Column(db.Text)

	email = db.Column(db.Text)
	verified_email = db.Column(db.Boolean)

	picture = db.Column(db.Text)

	company = db.Column(db.Text)
	address = db.Column(db.Text)
	city = db.Column(db.Text)
	state = db.Column(db.Text)
	postal_code = db.Column(db.Integer)
	
	bio = db.Column(db.Text)

	# 

	date_created = db.Column(db.DateTime, default=datetime.datetime.utcnow())
	date_modified = db.Column(db.DateTime, default=datetime.datetime.utcnow())


	friends = db.relationship('Friendship', backref='user', lazy='dynamic', foreign_keys='Friendship.user_id')
	# messages = db.relationship('Message', backref='sender', lazy='dynamic', foreign_keys='Message.user_id')
	# messages = db.relationship('Message', backref='receiver', lazy='dynamic', foreign_keys='Message.receiver_id')



	# @property
	# def serialize(self):
	# 	ans = {}

	# 	for key in self:
	# 		ans[key] = self[key]

	# 	return ans


	def __init__(self, google_id, name=None, title=None, given_name=None, family_name=None, gender=None, email=None, verified_email=None, picture=None, company=None, address=None, city=None, state=None, postal_code=None, bio=None):

		self.google_id = google_id
		self.name = name
		self.title = title
		self.given_name = given_name
		self.family_name = family_name
		self.gender = gender
		self.email = email
		self.verified_email = verified_email
		self.picture = picture
		self.company = company
		self.address = address
		self.city = city
		self.state = state
		self.postal_code = postal_code
		self.bio = bio

		# self.date_created = date_created
		# self.date_modified = date_modified



	# def __repr__(self):
	# 	return 'name: {name}, id: {id}'.format(name=self.name, id=self.id)

	# def __repr__(self):
	# return 'name: {name}, id: {id}, google_id: {google_id}'.format(name=self.name, id=self.id, google_id=self.google_id)

class Friendship(db.Model):
	__tablename__ = 'friendships'
	
	id = db.Column(db.Integer, primary_key=True)
	user_id = db.Column(db.Integer, db.ForeignKey('google_users.id')	
		)
	friend_id = db.Column(db.Integer, db.ForeignKey('google_users.id'))
	request_status = db.Column(db.Boolean)

	userID = db.relationship('GoogleUser', foreign_keys='Friendship.user_id')
	friendID = db.relationship('GoogleUser', foreign_keys='Friendship.friend_id')

	date_created = db.Column(db.DateTime, default=datetime.datetime.utcnow())

	def __init__(self, user_id, friend_id, request_status, date_created):
		
		self.user_id = user_id
		self.friend_id = friend_id
		self.request_status = request_status
		# self.date_created = date_created

	def __repr__(self):
		return 'user: {user}, friend: {friend}; status: {status}'.format(user=self.user_id, friend=self.friend_id, status=self.request_status)


class Conversation(db.Model):
	__tablename__= 'conversations'

	id = db.Column(db.Integer, primary_key=True)
	user_id = db.Column(db.Integer, db.ForeignKey('google_users.id'))
	receiver_id = db.Column(db.Integer, db.ForeignKey('google_users.id'))

	# TO ADD!!!
	date_created = db.Column(db.DateTime, default=datetime.datetime.utcnow())
	date_modified = db.Column(db.DateTime, default=datetime.datetime.utcnow())


	def __init__(self, user_id, receiver_id, date_created, date_modified):
		self.user_id = user_id
		self.receiver_id = receiver_id
		# self.date_created = date_created
		# self.date_modified = date_modified

	# def __repr__(self):
	# 	return 'user_id: {}, receiver_id: {}'.format(self.user_id, self.receiver_id)



class Message(db.Model):
	# CHANGE SUBJECT TO OCCASION
	__tablename__ = 'messages'

	id = db.Column(db.Integer, primary_key=True)
	user_id = db.Column(db.Integer, db.ForeignKey('google_users.id'))
	receiver_id = db.Column(db.Integer, db.ForeignKey('google_users.id'))
	occasion = db.Column(db.Text)
	content = db.Column(db.Text) 
	
	date = db.Column(db.Text)
	dateRangeFrom = db.Column(db.Integer)
	dateRangeUntil = db.Column(db.Integer)
	weekdaysMon = db.Column(db.Boolean)
	weekdaysTues = db.Column(db.Boolean)
	weekdaysWed = db.Column(db.Boolean)
	weekdaysThurs = db.Column(db.Boolean)
	weekdaysFri = db.Column(db.Boolean)
	weekdaysSat = db.Column(db.Boolean)
	weekdaysSun = db.Column(db.Boolean)
	timeRangeFrom = db.Column(db.Integer)
	timeRangeUntil = db.Column(db.Integer)

	date_created = db.Column(db.DateTime, default=datetime.datetime.utcnow())


	sender = db.relationship('GoogleUser', foreign_keys='Message.user_id')
	receiver = db.relationship('GoogleUser', foreign_keys='Message.receiver_id')

 
	def __init__(self, user_id, receiver_id, occasion, content, date, dateRangeFrom, dateRangeUntil, weekdaysMon, weekdaysTues, weekdaysWed, weekdaysThurs, weekdaysFri, weekdaysSat, weekdaysSun, timeRangeFrom, timeRangeUntil):
		
		self.user_id = user_id
		self.receiver_id = receiver_id
		self.occasion = occasion
		self.content = content
		self.date = date
		self.dateRangeFrom = dateRangeFrom
		self.dateRangeUntil = dateRangeUntil
		self.weekdaysMon = weekdaysMon
		self.weekdaysTues = weekdaysTues
		self.weekdaysWed = weekdaysWed
		self.weekdaysThurs = weekdaysThurs
		self.weekdaysFri = weekdaysFri
		self.weekdaysSat = weekdaysSat
		self.weekdaysSun = weekdaysSun
		self.timeRangeFrom = timeRangeFrom
		self.timeRangeUntil = timeRangeUntil
		# self.date_created = date_created

	# def __repr__(self):
	# 	return 'sender: {sender}, receiver: {receiver}, subject: {subject}, content: {content}'.format(sender=self.user_id, receiver=self.receiver_id, subject=self.subject, sticker=self.sticker, content=self.content )



# 
class G_UserSchema(ma.ModelSchema):
	class Meta:
		model = GoogleUser

		@post_load
		def make_user(self, data):
			return GoogleUser(**data)



class ConversationSchema(ma.ModelSchema):
	class Meta:
		model = Conversation 
		fields = ('id', 'user_id', 'receiver_id')



class MessagesSchema(Schema):
	
	# class Meta:
	id = fields.Integer()
	user_id = fields.Integer()
	receiver_id = fields.Integer()
	content = fields.String()

		# sender = fields.Nested('self')
		# receiver = fields.Nested('self')
		# model = Message 
		# id = fields.Integer()
		# user_id = fields.Integer()
		# receiver_id = fields.Integer()

		# fields = ('id', 
		# 		'user_id', 
		# 		'receiver_id', 
		# 		'occasion', 
		# 		'content', 
		# 		'date', 
		# 		'date_created',
		# 		'dateRangeFrom', 
		# 		'dateRangeUntil', 
		# 		'timeRangeFrom', 
		# 		'timeRangeUntil',
		# 		'weekdaysFri', 
		# 		'weekdaysMon', 
		# 		'weekdaysSat', 
		# 		'weekdaysSun'
		# 		'weekdaysThurs', 
		# 		'weekdaysTues', 
		# 		'weekdaysWed')

	@post_load
	def make_message(self, data):
		from IPython import embed; embed()
		return Message(**data)






# class MessagedUsers(ma.Schema):
# 	class Meta:
# 		fields = ()


	# 	fields = ('id', 'name', 'given_name', 'family_name', 'email', 'gender', 'picture', 'verified_email')
	# _links = ma.Hyperlinks({
	# 	'self': ma.URLFor('user_detail', id='<id>'),
	# 	'collection': ma.URLFor('users')
	# 	})


