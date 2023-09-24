from flask import Flask, render_template, request,redirect
from flask import Blueprint
from models.order import Order
from models.item import Item
from models.itemorder import ItemOrder
from app import db

itemorders_blueprint = Blueprint("itemorders", __name__)

@itemorders_blueprint.route("/itemorders")
def item_orders():
    item_orders = ItemOrder.query.all()
    return render_template("itemorders/index.jinja", item_orders = item_orders)

# creating an itemorder (UPDATE: these are now orders)
@itemorders_blueprint.route("/itemorders", methods=["POST"])
def create_itemorder():
    order_id = request.form['order_id']
    item_id = request.form['item_id']
    itemorder = ItemOrder(order_id = order_id, item_id=item_id)
    db.session.add(itemorder)
    db.session.commit()
    return redirect("/itemorders")

# creating a new itemorder
@itemorders_blueprint.route("/itemorders/new", methods=['GET'])
def new_itemorder():
    orders = Order.query.all()
    items = Item.query.all()
    return render_template("itemorders/new.jinja", orders = orders, items = items)

# deleting an itemorder
@itemorders_blueprint.route("/itemorders/<id>/delete", methods=["POST"])
def delete_visit(id):
    ItemOrder.query.filter_by(id =id).delete()
    db.session.commit()
    return redirect('/itemorders')