from flask import Flask, render_template, request, redirect
from flask import Blueprint
from models.customer import Customer
from models.item import Item
from models.order import Order
from app import db

items_blueprint = Blueprint("items", __name__)

@items_blueprint.route("/items")
def items():
    items = Item.query.all()
    # Item.query.delete()
    
    # customer1 = Customer(customer="Bella")
    # customer2 = Customer(customer="Sophia")

    # # item1 = Item(item_name="Babka", price=10)
    # # item2 = Item(item_name="Scone", price= 3)
    # # item3 = Item(item_name="Chocolate Chip Cookie", price=3)

    # db.session.add(customer1)
    # db.session.add(customer2)

    # # db.session.add(item1)
    # # db.session.add(item2) 
    # # db.session.add(item3)
    # db.session.commit() 

    return render_template("items/index.jinja", items = items)

# @items_blueprint.route("/items/<id>")
# def item_show(id):
#     item_to_show = Item.query.get(id)    
#     return render_template("items/show.jinja", item=item_to_show)
    