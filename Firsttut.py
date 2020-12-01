# import Flask class from flask
from flask import Flask
app = Flask(__name__)

# default route


@app.route('/')
def hello_world():
    return 'Hello World!'

# route to shailesh


@app.route('/shailesh')
def hello_shailesh():
    return 'Hello Shailesh!!!!'


app.run(debug=True)
