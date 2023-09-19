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


