from app import db

class Order(db.Model):
    __tablename__ = "orders"

    id = db.Column(db.Integer, primary_key=True)
    customer = db.Column(db.String(64))
    phone_number = db.Column(db.String(64))
    email = db.Column(db.String(64))
    itemorders = db.relationship("ItemOrder", backref="order")

    def __repr__(self):
        return f"<Order {self.id}: {self.customer}"
