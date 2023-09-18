from flask import Flask, render_template, request, redirect
from flask import Blueprint
# from models.order import Order
from models.item import Item
# from models.itemorder import ItemOrder

items_blueprint = Blueprint("items", __name__)

@items_blueprint.route("/items")
def items():
    items = Item.query.all()
    return render_template("items/index.jinja", items = items)

    