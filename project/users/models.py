from project import db, bcrypt, ma
from flask_login import UserMixin

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
	name = db.Column(db.Text)
	given_name = db.Column(db.Text)
	family_name = db.Column(db.Text)
	email = db.Column(db.Text)
	gender = db.Column(db.Text)
	google_id = db.Column(db.Text, unique=True)
	picture = db.Column(db.Text)
	verified_email = db.Column(db.Boolean)


	@property
	def serialize(self):
		ans = {}

		for key in self:
			ans[key] = self[key]

		return ans


	def __init__(self, name, given_name, family_name, email, gender, google_id, picture, verified_email):

		self.name = name
		self.given_name = given_name
		self.family_name = family_name
		self.email = email
		self.gender = gender
		self.google_id = google_id
		self.picture = picture
		self.verified_email = verified_email


	# def __repr__(self):
	# 	return 'name: {name}, id: {id}'.format(name=self.name, id=self.id)

	# def __repr__(self):
	# return 'name: {name}, id: {id}, google_id: {google_id}'.format(name=self.name, id=self.id, google_id=self.google_id)

class Friend(db.Model):
	__tablename__ = 'friends'

	user_id = db.Column(db.Integer, db.ForeignKey('google_users.id'), primary_key=True)
	friend_id = db.Column(db.Integer, db.ForeignKey('google_users.id'), primary_key=True)
	request_status = db.Column(db.Boolean)

	user = db.relationship('GoogleUser', foreign_keys='Friend.user_id')
	friend = db.relationship('GoogleUser', foreign_keys='Friend.friend_id')


	def __init__(self, user_id, friend_id, request_status):
		
		self.user_id = user_id
		self.friend_id = friend_id
		self.request_status = request_status

	def __repr__(self):
		return 'user: {user}, friend: {friend}; status: {status}'.format(user=self.user_id, friend=self.friend_id, status=self.request_status)




class Message(db.Model):
	__tablename__ = 'messages'

	id = db.Column(db.Integer, primary_key=True)
	sender_id = db.Column(db.Integer)
	receiver_id = db.Column(db.Integer)
	subject = db.Column(db.Text)
	sticker = db.Column(db.Text)
	content = db.Column(db.Text) 


	def __init__(self, sender_id, receiver_id, subject, sticker, content):
		
		self.sender_id = db.Column(db.Integer)
		self.receiver_id = db.Column(db.Integer)
		self.subject = db.Column(db.Text)
		self.sticker = db.Column(db.Text)
		self.content = db.Column(db.Text)

	def __repr__(self):
		return 'sender: {sender}, receiver: {receiver}, subject: {subject}, content: {content}'.format(sender=self.sender_id, receiver=self.receiver_id, subject=self.subject, sticker=self.sticker, content=self.content )



class G_UserSchema(ma.ModelSchema):
	class Meta:
		model = GoogleUser
	# 	fields = ('id', 'name', 'given_name', 'family_name', 'email', 'gender', 'picture', 'verified_email')
	# _links = ma.Hyperlinks({
	# 	'self': ma.URLFor('user_detail', id='<id>'),
	# 	'collection': ma.URLFor('users')
	# 	})


