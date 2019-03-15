from flask import Flask, render_template, redirect,url_for, request, flash
from flask_sqlalchemy import SQLAlchemy
import sqlite3
from flask import request
from flask_bootstrap import Bootstrap
import logging


logging.basicConfig(level=logging.DEBUG)
app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite://///Users/ewa_anna_szyszka/Desktop/Test/test.db'
db = SQLAlchemy(app)


class Todo(db.Model):
        id = db.Column(db.Integer, primary_key=True)
        text = db.Column(db.String(200))
        #complete = db.Column(db.Boolean) #Here you would need 3 statuses todo doing complete
        status = db.Column(db.String(100))
        #progress = db.Column(db.Boolean)


db.create_all()
db.session.commit()

@app.route('/')
def index():
        incomplete = Todo.query.filter_by(status='incomplete').all()
        inprogress = Todo.query.filter_by(status = 'inprogress').all()  #
        complete = Todo.query.filter_by(status = 'complete').all() #complete = True is in progress
        logging.debug(repr(incomplete))
        logging.debug(repr(inprogress))
        logging.debug(repr(complete))
        return render_template("index.html", incomplete=incomplete, inprogress=inprogress, complete=complete)

@app.route('/about')
def about():
    return render_template("about.html")

@app.route('/add', methods=['POST'])
def add():
    todo = Todo(text=request.form['todoitem'], status='incomplete')
    db.session.add(todo)
    db.session.commit()
    return redirect(url_for('index'))

@app.route('/asinprogress/<id>')
def asinprogress(id):
    todo = Todo.query.filter_by(id=int(id)).first()
    todo.status = 'inprogress'  #here set complete
    db.session.commit()
    return redirect(url_for('index'))

@app.route('/ascomplete/<id>')
def ascomplete(id):
    todo = Todo.query.filter_by(id=int(id)).first()
    todo.status = 'complete'  #here set complete
    db.session.commit()
    return redirect(url_for('index'))

@app.route('/delete', methods=['POST'])
def delete():
    imd = request.form
    form = imd.to_dict()
    task_id = next(iter(form))
    task = Todo.query.filter_by(id=int(task_id)).first()
    db.session.delete(task)
    db.session.commit()
    return redirect(url_for('index'))


if __name__ == '__main__':
    app.run(debug=True)
