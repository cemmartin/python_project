from flask import Flask, render_template, request, redirect
from flask import Blueprint
from models.customer import Customer
from models.order import Order
from models.item import Item
from models.orderItem import OrderItem
from app import db
import pdb

orders_blueprint = Blueprint("orders", __name__)


@orders_blueprint.route("/orders")
def orders():
    orders = Order.query.all()
    return render_template("orders/index.jinja", orders=orders)


@orders_blueprint.route("/orders/<id>")
def show_order(id):
    #     customer = Customer.query.get(order_to_show.customer_id)
    #     # print(order_to_show)
    #     # pdb.set_trace()
    #     return render_template("orders/show.jinja", order=order_to_show, customer=customer)
    order_to_show = Order.query.get(id)
    return render_template("orders/show.jinja", order=order_to_show)


# creating an order
@orders_blueprint.route("/orders", methods=["POST"])
def create_order():
    customer_id = request.form["customer_id"]
    # item_id = request.form['item_id']
    # tried to add item & itemorder back in & they didn't work
    order = Order(customer_id=customer_id)
    db.session.add(order)
    db.session.commit()
    return redirect("/orders")


# create order then add items to it
# creating a new ORDER
@orders_blueprint.route("/orders/new", methods=["GET"])
def new_order():
    customers = Customer.query.all()
    # items = Item.query.all()
    return render_template("orders/new.jinja", customers=customers)
    # return render_template("orders/new.jinja", customers=customers, items=items)


# deleting an ORDER
@orders_blueprint.route("/orders/<id>/delete", methods=["POST"])
def delete_order(id):
    Order.query.filter_by(id=id).delete()
    db.session.commit()
    return redirect("/orders")


# edit/update  - this is also where we'll be adding items
@orders_blueprint.route("/orders/<id>/edit", methods=["GET"])
def edit_order(id):
    customers = Customer.query.all()
    items = Item.query.all()
    orders = Order.query.all()
    orderItems = OrderItem.query.all()
    # get all the OrderItems for this order
    return render_template(
        "/orders/edit.jinja", id=id, customers=customers, items=items, orders=orders, orderItems=orderItems)


# not 100% sure about this
@orders_blueprint.route("/orders/<id>/edit", methods=["POST"])
def update_order(id):
    # pdb.set_trace()
    for item_id in request.form.getlist("item_ids"):
        new_orderItem = OrderItem(item_id=item_id, order_id=id)
        db.session.add(new_orderItem)
        db.session.commit()
    return redirect("/orders")

    # order = Order.query.get(id)
    # item_id = request.form.get("item")
    # item = Item.query.get(item_id)
    # if item:
    #     new_orderItem = OrderItem(item=item, order = order)
    #     db.session.add(new_orderItem)
    #     db.session.commit()
    # return redirect("/order")


# want to create new orderItem object w/ item id & order id & save to db
# request.form - going to have the list of check boxes in it & that's the lst you want to loop around
# item id will be the thing in each iteration


# Q's
# would i append anything???
# would there be any truethy/falsiness involved? If statement?
