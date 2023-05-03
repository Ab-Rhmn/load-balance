from flask import Flask, request


app = Flask(__name__)


@app.route('/sth', methods=['POST', 'GET'])
def hello():
    if request.method == 'GET':
        # Handle GET request
        return 'This is a GET request'
    elif request.method == 'POST':
        # Handle POST request
        data = request.form['data']
        return f'This is a POST request with data: {data}'
