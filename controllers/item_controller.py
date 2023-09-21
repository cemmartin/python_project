from flask import Flask, render_template, request, redirect
from flask import Blueprint
from models.order import Order
from models.item import Item
from models.itemorder import ItemOrder
from app import db

items_blueprint = Blueprint("items", __name__)

@items_blueprint.route("/items")
def items():
    items = Item.query.all()
    return render_template("items/index.jinja", items = items)

# @items_blueprint.route("/items/<id>")
# def item_show(id):
#     item_to_show = Item.query.get(id)    
#     return render_template("items/show.jinja", item=item_to_show)
    