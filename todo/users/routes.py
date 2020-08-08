from flask import render_template, url_for, request, flash, redirect, session
from todo.users.form import RegistrationForm, LoginForm
from todo import db, bcrypt
from todo.models import User

from flask import Blueprint

users = Blueprint('users', __name__)

@users.route("/login", methods=["POST", "GET"])
def login():
    
    if 'loggedin' in session:
        return redirect(url_for("main.index"))
    
    form = LoginForm()
    if form.validate_on_submit():
        user = User.query.filter_by(email=form.email.data).first()
        if user and bcrypt.check_password_hash(user.password, form.password.data):
            session['loggedin'] = True
            session['id']  = user.id
            session['username'] = user.name
            return redirect(url_for("main.index"))
        else:
            flash("Login failed, please check credentials", "danger")    
    return render_template("login.html", form=form)

@users.route("/register", methods=["GET", "POST"])
def register():
    if 'loggedin' in session:
        return "Already logged in"
    form = RegistrationForm()
    if form.validate_on_submit():
        account = User.query.filter_by(name=form.username.data).first()
        # print(f"account name {account}")
        if account:
            flash("This account is alredy exists", "danger")
        else:
            hashed_password = bcrypt.generate_password_hash(form.password.data).decode('utf-8')
            user = User(name=form.username.data, password=hashed_password, email=form.email.data)
            db.session.add(user)
            db.session.commit() 
            flash(f"Account created for {form.username.data}", "success")
            return redirect(url_for('users.login')) 
        
    return render_template("register.html", form=form)

    
@users.route("/logout", methods=["GET", "POST"])
def logout():
    session.clear()
    print(session)
#    session.pop('loggedin', None)
#    session.pop('id', None)
#    session.pop('username', None)
#    print(session)
    return redirect(url_for("users.login"))