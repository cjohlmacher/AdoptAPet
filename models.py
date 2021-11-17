from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

def connect_db(app):
    db.app = app
    db.init_app(app)


class Pet(db.Model):
    """ Defines pet model """

    __tablename__ = "pets"

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String, nullable=False)
    species = db.Column(db.String, nullable=False)
    photo_url = db.Column(db.String, nullable=True)
    age = db.Column(db.Integer, nullable=True)
    notes = db.Column(db.String, nullable=True)
    available = db.Column(db.String, nullable=False, default="True")

    def __repr__(self):
        pet = self
        return f"{pet.name}: {pet.species}, age {pet.age} - Availability: {pet.available}"


