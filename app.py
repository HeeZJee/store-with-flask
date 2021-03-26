from flask import Flask
app = Flask(__name__)

@app.route('/')
def index():
    return "<h2>It's Honme Page Boi</h2>"

@app.route('/greet/')
def hello_world():
    return 'Ello, World!'


@app.route('/user/<username>')
def show_user_profile(username):
    # show the user profile for that user
    return f'Hi Dear, {username}' 