from app import db

class Customer(db.Model):
    __tablename__ = "customers"

    id = db.Column(db.Integer, primary_key=True)
    customer = db.Column(db.String(64))
    phone_number = db.Column(db.String(64))
    email = db.Column(db.String(64))
    orders = db.relationship("Order", backref="customer")

    def __repr__(self):
        return f"<Customer {self.id}: {self.customer}"
