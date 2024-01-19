from app import db


class OrderItem(db.Model):
    __tablename__ = "orderItems"

    id = db.Column(db.Integer, primary_key=True)
    order_id = db.Column(db.Integer, db.ForeignKey("orders.id"))
    item_id = db.Column(db.Integer, db.ForeignKey("items.id"))
    # orders = db.relationship("Order", backref="order")
    
