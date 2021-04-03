from src import app
from flask import render_template
from typing import List
from src.models import Item
from src.forms import RegisterForm


# adding route for home page
@app.route('/')
@app.route('/home')
def index():
    return render_template("index.html")


# adding route for marekt page
@app.route('/market')
def market():

    items: List[object] = Item.query.all()
    # items: List[object] = [
    #     {'id': 1, 'name': 'Phone', 'barcode': '893212299897', 'price': 500},
    #     {'id': 2, 'name': 'Laptop', 'barcode': '123985473165', 'price': 900},
    #     {'id': 3, 'name': 'Keyboard', 'barcode': '231985128446', 'price': 150}
    # ]
    return render_template("market.html", items=items)


@app.route('/register')
def register():
    form = RegisterForm()
    return render_template('register.html', form=form)
