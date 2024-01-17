from flask import Flask, render_template, request,redirect
from flask import Blueprint
from models.customer import Customer
from models.order import Order
from models.item import Item
from app import db

orders_blueprint = Blueprint("orders", __name__)

@orders_blueprint.route("/orders")
def orders():
    orders = Order.query.all()
    return render_template("orders/index.jinja", orders=orders)

# creating an order
@orders_blueprint.route("/orders", methods=["POST"])
def create_order():
    customer_id = request.form['customer_id']
    item_id = request.form['item_id']
    order = Order(customer_id = customer_id, item_id = item_id)
    db.session.add(order)
    db.session.commit()
    return redirect("/orders")

# creating a new ORDER
@orders_blueprint.route("/orders/new", methods=['GET'])
def new_order():
    customers = Customer.query.all()
    items = Item.query.all()
    return render_template("orders/new.jinja", customers=customers, items = items)

# deleting an ORDER
@orders_blueprint.route("/orders/<id>/delete", methods=['POST'])
def delete_order(id):
    Order.query.filter_by(id =id).delete()
    db.session.commit()
    return redirect('/orders')

# Need to add edit & update here!! The below is not working & I can't figure out why :(


# @orders_blueprint("/orders/<id>/edit", methods=["GET"])
# def edit_order(id):
#     return render_template("/orders/edit.jinja", id=id) #need to add edit.jinja

# @orders_blueprint.route("/orders/<id>/update", methods=["POST"]) #not 100% sure this is the best way to go about this
# def update_order(id):
#     order = Order.query.get(id)
#     order.customer_id['customer_id']
#     order.item_id['item_id']
#     db.session.commit()
#     return redirect("/orders")



