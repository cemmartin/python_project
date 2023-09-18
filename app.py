from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate

app = Flask(__name__)

app.config["SQLALCHEMY_DATABASE_URI"] = f"postgresql://user@localhost:5432/proj1"
db = SQLAlchemy(app)
from models.order import Order
from models.item import Item
from models.itemorder import ItemOrder

mirgrate = Migrate(app, db)