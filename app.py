from flask import Flask, render_template
from flask_sqlalchemy import SQLAlchemy
from typing import List
app = Flask(__name__)


# configuring database URI
app.config["SQLALCHEMY_DATABASE_URI"] = 'sqlite:///market.db'
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = True

# connecting to database
db = SQLAlchemy(app)


# creating table for products
class Item(db.Model):
    id = db.Column(db.Integer(), primary_key=True)
    name = db.Column(db.String(length=30), nullable=False, unique=True)
    price = db.Column(db.Integer(), nullable=False)
    barcode = db.Column(db.String(length=8), nullable=False, unique=True)
    description = db.Column(db.String(length=1024), nullable=False, unique=True)

    def __repr__(self):
        return self.name



# adding route for home page
@app.route('/')
@app.route('/home')
def index():
    return render_template("index.html")


# adding route for marekt page
@app.route('/market')
def market():

    items = Item.query.all()
    # items: List(object) = [
    #     {'id': 1, 'name': 'Phone', 'barcode': '893212299897', 'price': 500},
    #     {'id': 2, 'name': 'Laptop', 'barcode': '123985473165', 'price': 900},
    #     {'id': 3, 'name': 'Keyboard', 'barcode': '231985128446', 'price': 150}
    # ]
    return render_template("market.html", items=items)


# @app.route('/user/<username>')
# def show_user_profile(username):
#     # show the user profile for that user
#     return f'Hi Dear, {username}'
