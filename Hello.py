from flask import Flask

app = Flask(__name__)

@app.route("/")
def hello_workd():
    return "<p>Hello, World!</p>"
    