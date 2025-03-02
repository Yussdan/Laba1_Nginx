from flask import Flask
app = Flask(__name__)

@app.route('/')
def home():
    return "Project 1: Hello HTTPS World!"