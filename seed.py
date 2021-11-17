from models import db, Pet
from app import app

#Create all tables in the database
db.drop_all()
db.create_all()

#Add Pets
pet_1 = Pet(name="Woofly", species="dog", photo_url="https://images.pexels.com/photos/4587996/pexels-photo-4587996.jpeg?auto=compress&cs=tinysrgb&w=1260&h=750&dpr=2", age=3, notes="Loves to eat waffles and run in the mud", available=True)
pet_2 = Pet(name="Porchetta",species="porcupine", photo_url="https://images.pexels.com/photos/5030891/pexels-photo-5030891.jpeg?auto=compress&cs=tinysrgb&w=1260&h=750&dpr=2", age=2, available=False)
pet_3 = Pet(name="Snargle", species="cat", photo_url="https://images.pexels.com/photos/991831/pexels-photo-991831.jpeg?auto=compress&cs=tinysrgb&w=1260&h=750&dpr=2", age=4, available=True)
for pet in [pet_1, pet_2, pet_3]:
    db.session.add(pet)
db.session.commit()
