import os
from flask import Flask;
from flask_sqlalchemy import SQLAlchemy;
from flask_bcrypt import Bcrypt


app = Flask(__name__);

# configuring database URI
app.config["SQLALCHEMY_DATABASE_URI"] = 'sqlite:///market.db';
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = True;
app.config['SECRET_KEY'] = os.environ.get('SECRET_KEY')

# connecting to database
db = SQLAlchemy(app);

# connecting to bcrypt to generate hash attributes
bcrypt = Bcrypt(app)

from src import routes