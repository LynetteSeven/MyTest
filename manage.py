from flask import Flask

app = Flask(__name__)

@app.route('/')
def index():
	print('Jackson')

	print('hahaha')

	print('manager')

	print('dev')

    return 'index1234'

if __name__ == '__main__':
    app.run(debug=True)