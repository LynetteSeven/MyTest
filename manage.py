from flask import Flask

app = Flask(__name__)

@app.route('/')
def index():
	print('Jackson')
    return 'index1234'

if __name__ == '__main__':
    app.run(debug=True)