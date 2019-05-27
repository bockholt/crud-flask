from flask_sqlalchemy import SQLAlchemy
db = SQLAlchemy()


class Cliente(db.Model):
    __tablename__ = 'cliente'
    _id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    email = db.Column(db.String)

    def __init__(self, email):
        self.email = email

