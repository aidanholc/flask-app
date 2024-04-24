from flask import Flask
app = Flask(__name__)

@app.route('/')
def hello_world():
    return 'Hello world!!! We\'ve upgraded from msoe the whole world can see this page!'