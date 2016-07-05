from flask import Flask, render_template, url_for, request
from flask_sqlalchemy import SQLAlchemy


app = Flask(__name__, static_path='/static')

app.config['SQLALCHEMY_DATABASE_URI'] = 'postgres://localhost/flink'
app.config['SQLALCHEMY_TRIACK_MODIFICATIONS'] = False


db = SQLAlchemy(app)

@app.route('/')
def index():
	return render_template('home.html')





if __name__ == '__main__':
	print('running on port 3000')
	app.run(debug=True, port=3000)
