from app import db
from models.customer import Customer
from models.item import Item
from models.order import Order
import click

from flask.cli import with_appcontext

@click.command(name="seed")
@with_appcontext
def seed():
    Item.query.delete()
    
    customer1 = Customer(name="Bella")
    customer2 = Customer(name="Sophia")

    item1 = Item(name="Babka")
    item2 = Item(name="Scone")
    item3 = Item(name="Chocolate Chip Cookie")


    db.session.add(customer1)
    db.session.add(customer2)

    db.session.add(item1)
    db.session.add(item2) 
    db.session.add(item3)

    db.session.commit()
    pass