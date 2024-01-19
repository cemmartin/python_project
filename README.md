# Read Me!

```
Major dependencies:
python3
postgresql

Start Guide:
pip3 install flask
pip3 install flask-sqlalchemy
pip3 install python-dotenv
pip3 install flask-migrate
pip3 install psycopg2

brew install postgresql@14 (this will only work on mac)

createdb bakery_app

In app.py:
app.config["SQLALCHEMY_DATABASE_URI"] = "postgresql://<your_postgres_user>@localhost:5432/bakery_app"

To run the application:
flask db init
flask db migrate
flask db upgrade
flask seed
flask run
```
