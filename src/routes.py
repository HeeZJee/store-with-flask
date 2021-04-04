from src import app
from flask import render_template, redirect, url_for, flash
from typing import List
from src.models import Item, User
from src.forms import LoginForm, RegisterForm
from src import db

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
# adding route for registration page


# adding route for registration page
@app.route('/login', methods=['GET', "POST"])
def login():
    form = LoginForm()
    return render_template('login.html', form=form)

# adding route for registration page
@app.route('/register',methods=['GET',"POST"])
def register():

    # create instance of form
    form = RegisterForm()

    #  adding data to database on clicking submit button
    if form.validate_on_submit():
        user_to_create = User(
            username=form.username.data,
            email=form.email.data,
            password_hash=form.password.data,
        )

        db.session.add(user_to_create)
        db.session.commit()
        return redirect(url_for('market'))

    #  checking for errors on creating user
    if form.errors != {}:
        for errors in form.errors.values():
            flash(errors)
    return render_template('register.html', form=form, category='danger')
