from flask import render_template, url_for,  redirect, session
from todo.users.form import  LoginForm
from todo import  db

import MySQLdb.cursors, datetime
from flask import Blueprint

main = Blueprint('main', __name__)


@main.route("/", methods=["GET", "POST"])
def index():

    form = LoginForm()
    if "loggedin" in session:
        
        # notes = Note.query.filter_by(user_id=session['id'])
        query = f"SELECT * FROM note WHERE user_id ='{session['id']}' AND deleted IS NULL ORDER BY done ASC"
        notes = db.engine.execute(query).fetchall()
        print(notes)
        return render_template("todo.html", user=session["username"], notes = notes)

    return redirect(url_for("users.register"))
       
