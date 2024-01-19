from app import db


class OrderItems(db.Model):
    __tablename__ = "ordersItems"

    id = db.Column(db.Integer, primary_key=True)
    order_id = db.Column(db.Integer, db.ForeignKey("orders.id"))
    item_id = db.Column(db.Integer, db.ForeignKey("items.id"))
    # orders = db.relationship("Order", backref="order")
