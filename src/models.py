import flask_login
import flask_sqlalchemy
from src import db, bcrypt, login_manager
from flask_login import UserMixin
"""
You will need to provide a user_loader callback. This callback is used to reload the user object from the user ID stored in the session. It should take the unicode ID of a user, and return the corresponding user object. For example:
"""
@login_manager.user_loader
def load_user(user_id):
    return User.query.get(int(user_id))

# creating table for users
class User(db.Model, UserMixin):
    id = db.Column(db.Integer(), primary_key=True)
    username = db.Column(db.String(length=30), nullable=False, unique=True)
    email = db.Column(db.String(length=50), nullable=False, unique=True)
    password = db.Column(db.String(length=60), nullable=False)
    budget = db.Column(db.Integer(), nullable=False, default=1000)
    item = db.relationship('Item', backref='owned_user', lazy=True)

    @property
    def password_hash(self):
        return self.password_hash
    
    @property
    def pretty_budget(self):
        if len(str(self.budget)) > 3:
            print(f"{str(self.budget)[:-3]},{str(self.budget)[-3:]} $")
            return f"{str(self.budget)[:-3]},{str(self.budget)[-3:]} $"
        else:
            print(self.budget)
            return f"{self.budget} $"

    @password_hash.setter
    def password_hash(self, plain_text_password):
        self.password = bcrypt.generate_password_hash(plain_text_password).decode('utf-8')
    
    def check_password_correction(self, attempted_password):
        return bcrypt.check_password_hash(self.password,attempted_password)

        
    def __repr__(self):
        return self.username

# creating table for products
class Item(db.Model):
    id = db.Column(db.Integer(), primary_key=True)
    name = db.Column(db.String(length=30), nullable=False, unique=True)
    price = db.Column(db.Integer(), nullable=False)
    barcode = db.Column(db.String(length=8), nullable=False, unique=True)
    description = db.Column(db.String(length=1024), nullable=False, unique=True)
    owner = db.Column(db.Integer(),db.ForeignKey('user.id'))

    def __repr__(self):
        return self.name
