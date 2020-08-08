from datetime import datetime
from todo import db

db.metadata.clear() 

class User(db.Model):
    __tablename__ = "user"
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(20), unique=True, nullable=False)
    email = db.Column(db.String(120), unique=True, nullable=False)
    password = db.Column(db.String(60), nullable=False)
    notes = db.relationship('Note', backref="author")

    def __init__(self, name, email, password):
        self.name = name
        self.email = email
        self.password = password
        

    def __repr__(self):
        return f"User('{self.id}','{self.name}','{self.email}', {self.notes})"


class Note(db.Model):
    __tablename__ = "note"
    id = db.Column(db.Integer, primary_key=True)
    text = db.Column(db.Text, nullable=False)
    done = db.Column(db.Boolean, default=False, nullable=False)
    deleted = db.Column(db.DateTime, nullable=True)
    created = db.Column(db.DateTime, nullable=False, default=datetime.utcnow)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)

    def __init__(self, text, user_id, done= 0):

        self.text = text
        self.done = done
        self.user_id = user_id

    def __repr__(self):
        return f"Note('{self.id}', {self.text}','{self.created}', '{self.user_id}')"