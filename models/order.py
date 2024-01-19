from app import db

class Order(db.Model):
    __tablename__= "orders"

    id = db.Column(db.Integer, primary_key=True)
    pickup_date = db.Column(db.String(30))
    customer_id = db.Column(db.Integer, db.ForeignKey('customers.id'))
    # Items = db.relationship("Item", backref="order")
    # item_id = db.Column(db.Integer, db.ForeignKey('items.id')) #remove here later