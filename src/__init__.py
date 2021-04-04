import os
from flask import Flask;
from flask_sqlalchemy import SQLAlchemy;
from flask_bcrypt import Bcrypt
from flask_login import LoginManager

app = Flask(__name__);

# configuring database URI
app.config["SQLALCHEMY_DATABASE_URI"] = 'sqlite:///market.db';
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = True;
app.config['SECRET_KEY'] = os.environ.get('SECRET_KEY')

# connecting to database
db = SQLAlchemy(app);

# connecting to bcrypt to generate hash attributes
bcrypt = Bcrypt(app)

# allowing flask login to manage user logins
login_manager = LoginManager()
login_manager.init_app(app)

from src import routes
