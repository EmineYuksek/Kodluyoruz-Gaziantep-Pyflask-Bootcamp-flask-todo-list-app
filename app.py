from flask import Flask,render_template, flash, redirect, url_for, session, logging
from data import Articles
from flask_sqlalchemy import SQLAlchemy
from wtforms import Form, StringField, TextAreaField, PasswordField, validators
from passlib.hash import sha256_crypt
from functools import wraps






app = Flask(__name__)

app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:////Users/okkes/Desktop/ToDoApp/Users.db'
db = SQLAlchemy(app)




Articles = Articles()




@app.route('/')
def index():
    return render_template('home.html')


@app.route('/about')
def about():
    return render_template('about.html')


@app.route('/articles')
def articles():
    return render_template('articles.html', articles = Articles)


@app.route('/article/<string:id>/')
def article(id):
    return render_template('articles.html', id = id)








class User(db.Model):
    __tablename__ = 'Users'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.VARCHAR(100))
    email = db.Column(db.VARCHAR(100))
    username = db.Column(db.VARCHAR(30))
    password = db.Column(db.VARCHAR(50))
    register_date = db.Column(db.TIMESTAMP)  #...

if __name__ == '__main__':
    app.run(debug=True) #debeggur aktif etme

