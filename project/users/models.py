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
		return 'name: {1} - password: {2}'.format(self.name, self.password)


