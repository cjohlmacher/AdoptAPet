from flask import Flask, request, render_template, flash, redirect, session
from flask_debugtoolbar import DebugToolbarExtension
from models import db, connect_db, Pet
from forms import PetForm, EditPetForm

app = Flask(__name__)

app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql:///adopt'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['SQLALCHEMY_ECHO'] = True
app.config['SECRET_KEY'] = "placeholder"
app.config['DEBUG_TB_INTERCEPT_REDIRECTS'] = False
debug = DebugToolbarExtension(app)

connect_db(app)

@app.route('/')
def show_home_page():
    pets = Pet.query.order_by('id').all()
    return render_template('home.html', pets=pets)

@app.route('/add', methods=['GET','POST'])
def add_pet():
    form = PetForm()
    if form.validate_on_submit():
        name = form.name.data
        species = form.species.data
        photo_url = form.photo_url.data
        age = form.age.data
        notes = form.notes.data
        available = form.available.data
        print('Available: ',available)
        new_pet = Pet(name=name, species=species, photo_url=photo_url, age=age, notes=notes, available=available)
        db.session.add(new_pet)
        db.session.commit()
        return redirect('/')
    else:
        return render_template('add-pet.html',form=form)

@app.route('/<int:pet_id>')
def view_pet(pet_id):
    pet = Pet.query.get_or_404(pet_id)
    return render_template('pet-info.html',pet=pet)

@app.route('/<int:pet_id>/edit', methods=['GET','POST'])
def edit_pet(pet_id):
    pet = Pet.query.get_or_404(pet_id)
    print('Pet available: ',pet.available)
    form = EditPetForm(obj=pet)
    if form.validate_on_submit():
        pet.photo_url = form.photo_url.data
        pet.notes = form.notes.data
        pet.available = form.available.data
        db.session.add(pet)
        db.session.commit()
        return redirect(f"/{pet.id}")
    else:
        return render_template('edit-pet.html',pet=pet, form=form)
