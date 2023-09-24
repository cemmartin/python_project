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

# show an order (UPDATE: will show a customer)
@orders_blueprint.route("/orders/<id>") 
def show_order(id):
    order_to_show = Order.query.get(id)
    return render_template("orders/show.jinja", order=order_to_show)

# create new customer
@orders_blueprint.route("/orders", methods=["POST"])
def create_order():
    customer = request.form["customer"]
    phone_number = request.form["phone_number"]
    email = request.form['email']
    customer_to_save = Order(customer= customer, phone_number=phone_number, email=email)
    db.session.add(customer_to_save)
    db.session.commit()
    return redirect("/orders")


# delete a customer --> maybe on the show page? or would customers page be more convenient?
@orders_blueprint.route("/orders/<id>/delete", methods=["POST"])
def remove_order(id):
    customer = Order.query.get(id)
    db.session.delete(customer)
    db.session.commit()
    return redirect("/orders")

#edit a customer --> not sure how to display this best in the css
@orders_blueprint.route("/orders/<id>", methods=["POST"])
def update_order(id):
    order = Order.query.get(id)
    order.customer = request.form["customer"]
    order.phone_number = request.form["phone_number"]
    order.email = request.form["email"]
    db.session.commit()
    redirect_order = "/orders" + "/id" #SOMETHING IS WRONG HERE
    return redirect(redirect_order)







# ###########################

# @orders_blueprint.route("/orders/<id>")
# def show(id):
#     order = Order.query.get(id)
#     items_that_have_been_ordered = Item.query.join(ItemOrder).filter(ItemOrder.order_id == id)
#     return render_template("orders/show.jinja", order=order, items=items_that_have_been_ordered)



    

# # new orders (now customers)
# @orders_blueprint.route("/orders/new", methods=['GET'])
# def new_order():


#need to be able to add new customers & delete exisint customers
    