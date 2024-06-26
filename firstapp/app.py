''' A simple hello world application that is hosted on a local server. '''
from flask import Flask


app = Flask(__name__)

@app.route("/")
def index():
    ''' The main route of the application. '''
    return "Hello, World!"


if __name__ == '__main__':
    app.run(port=5000, debug=True)