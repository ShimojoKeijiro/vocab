from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

class Word(db.Model):
    __tablename__ = 'words'
    id = db.Column(db.Integer, primary_key=True)
    japanese = db.Column(db.String(128), nullable=False)
    english = db.Column(db.String(128), nullable=False)
    note = db.Column(db.String(256))
