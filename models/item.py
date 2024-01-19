from app import db

class Item(db.Model):
    __tablename__ = "items"

    id = db.Column(db.Integer, primary_key=True)
    item_name = db.Column(db.String(64))
    price = db.Column(db.Integer)
    orderItems = db.relationship("OrderItem", backref="item") 
        # added above
    # orders = db.relationship("Order", backref="item") #would I remove this?

    def __repr__(self):
        return f"<{self.id}: {self.item_name}, {self.price}>"