from flask import Flask

app = Flask(__name__)


@app.route("/")
def create_user():
    return "<p>Hello User</p>"


@app.route("/hello")
def get_users():
    return "<p>Hello Users</p>"
