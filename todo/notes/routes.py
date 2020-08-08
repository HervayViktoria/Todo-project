from flask import  request, session
from todo import  db
from todo.models import Note
import datetime
from flask import Blueprint

notes = Blueprint('notes', __name__)


@notes.route("/create", methods=["GET", "POST"])
def create_note():
    if request.method == "POST":
        new_note = Note(user_id=session['id'], text=request.form['note'])
        db.session.add(new_note)
        db.session.commit()
        # cur = mysql.connection.cursor()
        # cur.execute(f"INSERT INTO `notes`(`user_id`, `text`) VALUES ({session['id']},'{request.form['note']}')")
        # mysql.connection.commit()
        # id = cur.lastrowid
        return str(new_note.id)

@notes.route("/update", methods=["GET", "POST"])
def update_note():
    if request.method == "POST":
        request_data_list = request.form['update_data'].split(',')
        # print(request_data_list)
        id = int(request_data_list[0])
        done = int(request_data_list[1])
        if done == 1:
            done = True
        else:
            done = False
     
        query = f"UPDATE note SET done = {done} WHERE id ={id}"
       
        db.engine.execute(query)

        return "update is ok"

@notes.route("/delete", methods=["GET", "POST"])
def delete_note():
    needed_date_format = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    if request.method == "POST":
        reqested_id = int(request.form['id'])

        query = f"UPDATE note SET deleted='{needed_date_format}' WHERE id = {reqested_id}"
        db.engine.execute(query)
        return "delete is ok"
    