from flask import Flask, render_template
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate

app = Flask(__name__)

app.config["SQLALCHEMY_DATABASE_URI"] = f"postgresql://user@localhost:5432/proj1"
app.config["SQLALCHEMY_ECHO"] = True
db = SQLAlchemy(app)
mirgrate = Migrate(app, db)
# from seed import seed

# from models.order import Order
# from models.item import Item
# from models.itemorder import ItemOrder



from controllers.item_controller import items_blueprint
from controllers.order_controller import orders_blueprint
from controllers.itemorder_controller import itemorders_blueprint

app.register_blueprint(items_blueprint)
app.register_blueprint(orders_blueprint)
app.register_blueprint(itemorders_blueprint)

@app.route('/')
def home():
    return render_template('index.jinja')

if __name__ == '__main__':
    app.run(debug=True)