from flask import Flask, render_template, request, redirect, url_for
from flask import Blueprint
from models.customer import Customer
from models.item import Item
from models.order import Order
from app import db

customers_blueprint = Blueprint("customers", __name__)

@customers_blueprint.route("/customers")
def customers():
    customers = Customer.query.all()
    return render_template("customers/index.jinja", customers=customers)

# show an order (UPDATE: will show a customer)
@customers_blueprint.route("/orders/<id>") 
def show_customer(id):
    customer_to_show = Customer.query.get(id)
    return render_template("orders/show.jinja", customer=customer_to_show)

# create new customer
@customers_blueprint.route("/customers", methods=["POST"])
def create_customer():
    customer = request.form["customer"]
    phone_number = request.form["phone_number"]
    email = request.form['email']
    customer_to_save = Customer(customer= customer, phone_number=phone_number, email=email)
    db.session.add(customer_to_save)
    db.session.commit()
    return redirect("/customers")


# delete a customer
@customers_blueprint.route("/customers/<id>/delete", methods=["POST"])
def remove_customer(id):
    customer = Customer.query.get(id)
    db.session.delete(customer)
    db.session.commit()
    return redirect("/customers")

# edit a customer --> not currently work; just adding new submission instead of actually editing the existing
@customers_blueprint.route("/customers/<id>/edit", methods=["GET"])
def edit_customer(id):
    return render_template("/customers/edit.jinja", id=id)  #preventing the redirect from happening    #
    # return redirect("/customers.index") #


#update a customer (from edit)
@customers_blueprint.route("/customers/<id>/update", methods = ["POST"]) #would this be /update
# @customers_blueprint.route("/customers/<id>", methods=["POST"])
def update_customer(id):
    customer = Customer.query.get(id)
    customer.customer = request.form['customer']
    customer.phone_number = request.form['phone_number']
    customer.email = request.form['email']
    db.session.commit()
    return redirect("/customers")
    # return redirect(url_for('customers.index'))




















#everything below here should be customer(s) not order(s)

    # order = Order.query.get(id)
    # order.customer = request.form["customer"]
    # order.phone_number = request.form["phone_number"]
    # order.email = request.form["email"]
    # db.session.commit()

    # redirect_order = "/orders" + "/<id>" #SOMETHING IS WRONG HERE
    # return redirect(redirect_order)



# @orders_blueprint.route("/orders/<id>", methods=["GET"])
# def update_order(id):





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
    