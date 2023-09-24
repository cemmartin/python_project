from app import db
from models.order import Order
from models.item import Item
import click

# from flask.cli import with_appcontext

# @click.command(name="seed")
# @with_appcontext
# def seed():
#     Item.query.delete()
    

# #     order1 = Order(name="Bella")
# #     order2 = Order(name="Sophia")

#     item1 = Item(name="Babka")
#     item2 = Item(name="Scone")
#     item3 = Item(name="Chocolate Chip Cookie")

# #     db.session.add(order1)
# #     db.session.add(order2)

#     db.session.add(item1)
#     db.session.add(item2) 
#     db.session.add(item3)
#     db.session.commit()  