from flask_wtf import FlaskForm
from wtforms import StringField, IntegerField, BooleanField, SelectField, TextAreaField
from wtforms.validators import InputRequired, Optional, NumberRange, Regexp

class PetForm(FlaskForm):
    name = StringField("Pet Name: ",validators=[InputRequired()])
    species = SelectField("Species: ",choices=[('dog','Dog'),('cat','Cat'),('porcupine','Porcupine')],validators=[InputRequired()])
    photo_url = StringField("Image URL: ",validators=[Optional(),Regexp("https://.*")])
    age = IntegerField("Age: ",validators=[Optional(),NumberRange(0,30)])
    notes = TextAreaField("Notes: ")
    available = BooleanField("Available: ")

class EditPetForm(FlaskForm):
    photo_url = StringField("Image URL: ",validators=[Optional(),Regexp("https://.*")])
    notes = TextAreaField("Notes: ")
    available = BooleanField("Available: ")