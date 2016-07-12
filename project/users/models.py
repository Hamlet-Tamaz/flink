from project import db, bcrypt
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

	id = db.Column(db.Text, primary_key=True)
	name = db.Column(db.Text)
	given_name = db.Column(db.Text)
	family_name = db.Column(db.Text)
	email = db.Column(db.Text)
	gender = db.Column(db.Text)
	# google_id = db.Column(db.Text)
	picture = db.Column(db.Text)
	verified_email = db.Column(db.Boolean)

	def __init__(self, name, given_name, family_name, email, gender, id, picture, verified_email):
		
		self.id = id
		self.name = name
		self.given_name = given_name
		self.family_name = family_name
		self.email = email
		self.gender = gender
		# self.google_id = google_id
		self.picture = picture
		self.verified_email = verified_email


	def __repr__(self):
		return 'name: {name}, id: {id}'.format(name=self.name, id=self.id)

	# def __repr__(self):
	# return 'name: {name}, id: {id}, google_id: {google_id}'.format(name=self.name, id=self.id, google_id=self.google_id)
