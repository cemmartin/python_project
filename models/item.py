from app import db

class Item(db.Model):
    __tablename__ = "items"

    id = db.Column(db.Integer, primary_key=True)
    item_name = db.Column(db.String(64))
    price = db.Column(db.Integer)
    itemorders = db.relationship("ItemOrder", backref="item")

    def __repr__(self):
        return f"<{self.id}: {self.item_name}, {self.price}>"