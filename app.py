from flask import Flask, render_template
app = Flask(__name__)

@app.route('/')
@app.route('/home')
def index():
    return render_template("index.html")

@app.route('/market')
def market():
    items = [
    {'id': 1, 'name': 'Phone', 'barcode': '893212299897', 'price': 500},
    {'id': 2, 'name': 'Laptop', 'barcode': '123985473165', 'price': 900},
    {'id': 3, 'name': 'Keyboard', 'barcode': '231985128446', 'price': 150}
]
    return render_template("market.html", items=items)
# @app.route('/')
# def index():
#     return "<h2>It's Honme Page Boi</h2>"


# @app.route('/greet/')
# def hello_world():
#     return 'Ello, World!'


# @app.route('/user/<username>')
# def show_user_profile(username):
#     # show the user profile for that user
#     return f'Hi Dear, {username}' 