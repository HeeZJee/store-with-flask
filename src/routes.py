from flask.globals import request
from src import app
from flask import render_template, redirect, url_for, flash, request
from typing import List
from src.models import Item, User
from src.forms import LoginForm, RegisterForm, PurchaseItem, SellItem
from src import db
from flask_login import login_user, login_required, logout_user, current_user

# adding route for home page


@app.route('/')
@app.route('/home')
def index():
    return render_template("index.html")


# adding route for marekt page
@app.route('/market', methods=["GET", "POST"])
@login_required
def market():
    purchase_form = PurchaseItem()
    selling_form = SellItem()

    if request.method == "POST":

        purchase_item = request.form.get("purchase_item")
        p_item_obj = Item.query.filter_by(name=purchase_item).first()
        
        sold_item = request.form.get("sold_item")
        s_item_obj = Item.query.filter_by(name=sold_item).first()
        if s_item_obj:
            if current_user.can_sell(s_item_obj):
                s_item_obj.sell(current_user)
                flash(
                    f"Congratulations! You sold {s_item_obj.name} for {s_item_obj.price}", category='success')
            else:
                flash(
                    f"Unfortunately! Something went wrong on selling {s_item_obj.name}", category="danger")

        return redirect(url_for('market'))
            

        # Handling request for purchase
        if p_item_obj:
            if current_user.can_purchase(p_item_obj):
                p_item_obj.buy(current_user)
                flash(
                    f"Congratulations! You purchased {p_item_obj.name} for {p_item_obj.price}", category='success')
            else:
                flash(
                    f"Unfortunately! You don't have enough money to purchase {p_item_obj.name}", category="danger")

        return redirect(url_for('market'))
    # Listing Items on Market page for sale
    if request.method == "GET":
        items: List[object] = Item.query.filter_by(owner=None)
        owned_items = Item.query.filter_by(owner=current_user.id)

        return render_template("market.html", items=items, purchase_form=purchase_form, owned_items=owned_items, selling_form=selling_form)


# adding route for registration page
@app.route('/login', methods=['GET', "POST"])
def login():
    form = LoginForm()
    if form.validate_on_submit():

        attempted_user = User.query.filter_by(
            username=form.username.data).first()

        if attempted_user and attempted_user.check_password_correction(attempted_password=form.password.data):
            login_user(attempted_user)
            flash(
                f"Success! you are logged in as {attempted_user.username}", category='success')
            return redirect(url_for('market'))
        else:
            flash("Username and Password are not match please try again.",
                  category='danger')
    return render_template('login.html', form=form)


# adding route for registration page
@app.route('/register', methods=['GET', "POST"])
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
        flash(
            f"Successfully registered! you are logged in as {user_to_create.username}", category='success')

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
