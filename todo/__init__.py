from flask import Flask, request
from flask_sqlalchemy import SQLAlchemy
from flask_bcrypt import Bcrypt
from flask_mysqldb  import MySQL


app = Flask(__name__)

ENV = "dev"
if ENV == "dev":
    app.debug = True
    app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://postgres:Televizio01@localhost/todo'

else:
    app.debug = False
    app.config['SQLALCHEMY_DATABASE_URI'] = 'postgres://hynfwiadkrpdku:2fa7fe21d8d6471a5fdfb7edb0e82e73cf19607321cfaa84a87e7db1a6775a59@ec2-54-217-224-85.eu-west-1.compute.amazonaws.com:5432/dcq1m3p8di9u3g'


app.config['SECRET_KEY'] = 'fc6c87ddd0786f0ce173f34e60720f1e'
# app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///todo.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False


db = SQLAlchemy(app)
bcrypt = Bcrypt(app)

from todo.users.routes import users
app.register_blueprint(users)

from todo.notes.routes import notes
app.register_blueprint(notes)

from todo.main.routes import main
app.register_blueprint(main)