from flask import Flask, render_template, request, redirect
from flask import Blueprint
# from models.order import Order
# from models.item import Item
from models.itemorder import ItemOrder
# from app import db

itemorders_blueprint = Blueprint("itemorders", __name__)

@itemorders_blueprint("/itemorders")
def item_orders():
    item_orders = ItemOrder.query.all()
    return render_template("itemorders/index.jinja", item_orders = item_orders)