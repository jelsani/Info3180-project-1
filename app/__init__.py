from flask import Flask
from flask_login import LoginManager
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config['SECRET_KEY'] = "secretkey"
app.config['SQLALCHEMY_DATABASE_URI'] = "postgresql://project1:password123@localhost/project1"
# postgresql://xloqvullykfxex:300ac5ecaa9f05a003e885ea6186d1813677a8300a465c7e3aedc3600da09599@ec2-75-101-133-29.compute-1.amazonaws.com:5432/dd4ecd3bh42she"
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = True # added just to suppress a warning 
app.config['UPLOAD_FOLDER']="./app/static/uploads"

db = SQLAlchemy(app) 



app.config.from_object(__name__)
from app import views
