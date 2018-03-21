from flask import Flask
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config['SECRET_KEY'] = "change this to be a more random key"
app.config['SQLALCHEMY_DATABASE_URI'] = 'postgres://futytvyyqdkjmo:ab6f2b3ae67b3060d7dfaa1a6ab93136cd66c9619877984a2a085d6f8edff789@ec2-54-235-146-51.compute-1.amazonaws.com:5432/dbq94ur2tia80h'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = True # added just to suppress a warning
app.config['UPLOAD_FOLDER'] = "./app/static/uploads"

db = SQLAlchemy(app)

app.config.from_object(__name__)
from app import views