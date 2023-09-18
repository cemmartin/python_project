from flask import Flask, render_template, request, redirect
from flask import Blueprint
from models.order import Order
# from models.item import Item
# from models.itemorder import ItemOrder

order_blueprint = Blueprint("orders", __name__)

@order_blueprint.route("/orders")
def orders():
    orders = Order.query.all()
    return render_template("users/index.jinja", orders = orders)
