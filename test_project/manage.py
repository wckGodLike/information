from flask import Flask

app = Flask(__name__）

@app.route('/')
def index():
	return 'index page'

@app.route('/user',methods =['POST','GET'])
def user():
	return 'user page'


if __name__ == '__main__':
	app.run()
