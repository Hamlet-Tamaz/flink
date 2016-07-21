from project import app
import os

port = os.environ.get('PORT')
debug = os.environ.get('DEBUG')

if __name__ == '__main__':
	print('running on port 3000')
	app.run(debug=debug, port=port)


