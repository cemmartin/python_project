from flask import Flask, render_template, request, redirect
from flask import Blueprint
from models.order import Order
from models.item import Item
from models.itemorder import ItemOrder
from app import db

orders_blueprint = Blueprint("orders", __name__)

@orders_blueprint.route("/orders")
def orders():
    orders = Order.query.all()
    return render_template("orders/index.jinja", orders = orders)

# show an order (now customer)
@orders_blueprint.route("/items/<id>")
def show_order(id):
    order_to_show = Order.query.get(id)
    return render_template("orders/show.jinja", order=order_to_show)


# @orders_blueprint.route("/orders/<id>")
# def show(id):
#     order = Order.query.get(id)
#     items_that_have_been_ordered = Item.query.join(ItemOrder).filter(ItemOrder.order_id == id)
#     return render_template("orders/show.jinja", order=order, items=items_that_have_been_ordered)



    

# # new orders (now customers)
# @orders_blueprint.route("/orders/new", methods=['GET'])
# def new_order():

    