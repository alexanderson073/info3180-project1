from flask import Flask
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config['SECRET_KEY'] = "change this to be a more random key"
app.config['SQLALCHEMY_DATABASE_URI'] = 'postgres://uaiuywvgrupapm:7d72109f2ad142cbbf5dc43f55529dd6aac6f0c117f0f6dc1ef23b7df81bc5bb@ec2-54-235-146-51.compute-1.amazonaws.com:5432/da68rbtv9p0i51'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = True # added just to suppress a warning
app.config['UPLOAD_FOLDER'] = "./app/static/uploads"

db = SQLAlchemy(app)

app.config.from_object(__name__)
from app import views