from src import db;

# creating table for products
class Item(db.Model):
    id = db.Column(db.Integer(), primary_key=True)
    name = db.Column(db.String(length=30), nullable=False, unique=True)
    price = db.Column(db.Integer(), nullable=False)
    barcode = db.Column(db.String(length=8), nullable=False, unique=True)
    description = db.Column(db.String(length=1024),
                            nullable=False, unique=True)

    def __repr__(self):
        return self.name