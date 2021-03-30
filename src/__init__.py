from flask import Flask;
from flask_sqlalchemy import SQLAlchemy;
app = Flask(__name__);

# configuring database URI
app.config["SQLALCHEMY_DATABASE_URI"] = 'sqlite:///market.db';
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = True;

# connecting to database
db = SQLAlchemy(app);


from src import routes;