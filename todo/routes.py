from flask import render_template, url_for, request, flash, redirect, session
from todo.forms.users import RegistrationForm, LoginForm
from todo import  app, db, bcrypt
from todo.models import User, Note
import MySQLdb.cursors, datetime

@app.route("/", methods=["GET", "POST"])
def index():

    form = LoginForm()
    if "loggedin" in session:

        # notes = Note.query.filter_by(user_id=session['id'])
        query = f"SELECT * FROM `note` WHERE `user_id` ='{session['id']}' AND `deleted` IS NULL"
        notes = db.engine.execute(query).fetchall()
        print(notes)
        return render_template("todo.html", user=session["username"], notes = notes)

    return redirect(url_for("login"))
       

@app.route("/create", methods=["GET", "POST"])
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

@app.route("/update", methods=["GET", "POST"])
def update_note():
    if request.method == "POST":
        request_data_list = request.form['update_data'].split(',')
        # print(request_data_list)
        id = request_data_list[0]
        done = request_data_list[1]

        query = f"UPDATE `note` SET `done`={done} WHERE `id` ={id}"
        notes = db.engine.execute(query)

        return "ok"

@app.route("/delete", methods=["GET", "POST"])
def delete_note():
    needed_date_format = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    if request.method == "POST":
        reqested_id = request.form['id']

        query = f"UPDATE `note` SET `deleted`='{needed_date_format}' WHERE `id` = {reqested_id}"
        db.engine.execute(query)
        return "ok"
    


@app.route("/login", methods=["POST", "GET"])
def login():
    
    if 'loggedin' in session:
        return redirect(url_for("index"))
    
    form = LoginForm()
    if form.validate_on_submit():
        user = User.query.filter_by(email=form.email.data).first()
        if user and bcrypt.check_password_hash(user.password, form.password.data):
            session['loggedin'] = True
            session['id']  = user.id
            session['username'] = user.name
            return redirect(url_for("index"))
        else:
            flash("Login failed, pleaase check credentials", "danger")    
    return render_template("login.html", form=form)

@app.route("/register", methods=["GET", "POST"])
def register():
    if 'loggedin' in session:
        return "Already logged in"
    form = RegistrationForm()
    if form.validate_on_submit():
        account = User.query.filter_by(name=form.username.data)
        if account:
            flash("This account is alredy exists", "danger")
        else:
            hashed_password = bcrypt.generate_password_hash(form.password.data).decode('utf-8')
            user = User(name=form.username.data, password=hashed_password, email=form.email.data)
            db.session.add(user)
            db.session.commit()
            flash(f"Account created for {form.username.data}", "success")
            return redirect(url_for('login')) 
        
    return render_template("register.html", form=form)

    
@app.route("/logout", methods=["GET", "POST"])
def logout():
    session.clear()
    print(session)
#    session.pop('loggedin', None)
#    session.pop('id', None)
#    session.pop('username', None)
#    print(session)
    return redirect(url_for("login"))
