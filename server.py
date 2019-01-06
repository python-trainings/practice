from flask import Flask
from flask import jsonify


app = Flask(__name__)

@app.route('/welcome')
def welcome():
    return jsonify({ "key" : "Welocme.....Hello"})

@app.route('/welcome/home')
def welcome_home():
    return "Home Page"

@app.route('/')
def index():
    return "ROOT........."

app.run()