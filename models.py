from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

class Patient(db.Model):

    id = db.Column(db.Integer, primary_key=True)

    age = db.Column(db.Integer)

    tumor_size = db.Column(db.Float)

    depth = db.Column(db.String(50))

    mitotic_count = db.Column(db.Integer)

    cellularity = db.Column(db.String(50))

    necrosis = db.Column(db.String(50))

    location = db.Column(db.String(100))

    prediction = db.Column(db.String(100))

    confidence = db.Column(db.Float)