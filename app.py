from flask import Flask
app = Flask(__name__)
@app.route("/")
def index():
    return "Hello"
@app.route("/home")
def home():
    return "Home Page"
if _name=="main_":
    app.run(host='0.0.0.0',port=1000)