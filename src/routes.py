from src import app
from flask import render_template, redirect, url_for, flash
from typing import List
from src.models import Item, User
from src.forms import LoginForm, RegisterForm
from src import db
from flask_login import login_user, login_required, logout_user

# adding route for home page
@app.route('/')
@app.route('/home')
def index():
    return render_template("index.html")


# adding route for marekt page
@app.route('/market')
@login_required
def market():

    items: List[object] = Item.query.all()

    return render_template("market.html", items=items)


# adding route for registration page
@app.route('/login', methods=['GET', "POST"])
def login():
    form = LoginForm()
    if form.validate_on_submit():
        
        attempted_user = User.query.filter_by(username=form.username.data).first()

        if attempted_user and attempted_user.check_password_correction(attempted_password=form.password.data):
            login_user(attempted_user)
            flash(f"Success! you are logged in as {attempted_user.username}", category='success')
            return redirect(url_for('market'))
        else:
            flash("Username and Password are not match please try again.",
                  category='danger')
    return render_template('login.html', form=form)

# adding route for registration page
@app.route('/register',methods=['GET',"POST"])
def register():

    # create instance registration of form
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
        
        login_user(user_to_create)
        flash(f"Successfully registered! you are logged in as {user_to_create.username}", category='success')

        return redirect(url_for('market'))

    #  checking for errors on creating user
    if form.errors != {}:
        for errors in form.errors.values():
            flash(errors, category='danger')
    return render_template('register.html', form=form)

@app.route('/logout')
def logout():
    logout_user()
    flash("You have been logged out.", category='info')
    return redirect(url_for("index"))
