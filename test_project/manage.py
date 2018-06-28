from flask import Flask

app = Flask(__name__）

@app.route('/')
def index():
	return 'index page'

a = 0
c = 1

if __name__ == '__main__':
	app.run()
