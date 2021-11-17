from models import db, Pet
from app import app

#Create all tables in the database
db.drop_all()
db.create_all()

#Add Pets
pet_1 = Pet(name="Woofly", species="dog", photo_url="https://images.pexels.com/photos/4587996/pexels-photo-4587996.jpeg?auto=compress&cs=tinysrgb&w=1260&h=750&dpr=2", age=3, notes="Loves to eat waffles and run in the mud", available=True)
pet_2 = Pet(name="Porchetta",species="porcupine", photo_url="https://images.pexels.com/photos/5030891/pexels-photo-5030891.jpeg?auto=compress&cs=tinysrgb&w=1260&h=750&dpr=2", age=2, available=False)
pet_3 = Pet(name="Snargle", species="cat", photo_url="https://images.pexels.com/photos/991831/pexels-photo-991831.jpeg?auto=compress&cs=tinysrgb&w=1260&h=750&dpr=2", age=4, available=True)
pet_4 = Pet(name="Warbles", species="cat", photo_url="https://images.pexels.com/photos/3687957/pexels-photo-3687957.jpeg?auto=compress&cs=tinysrgb&h=750&w=1260", age=3, notes="Camera shy", available=True)
pet_5 = Pet(name="Happy", species="dog", notes="Age of this pet is unknown", available=True)
pet_6 = Pet(name="Wookie", species="dog", photo_url="https://images.pexels.com/photos/5255205/pexels-photo-5255205.jpeg?auto=compress&cs=tinysrgb&w=1260&h=750&dpr=2", notes="This guy is ancient", age=30, available=True)
pet_7 = Pet(name="Fluffles", species="cat", photo_url="https://images.pexels.com/photos/1741205/pexels-photo-1741205.jpeg?auto=compress&cs=tinysrgb&w=1260&h=750&dpr=2", age=5, notes="Dresses to impress all the other cats at the tuxedo party", available=False)
pet_8 = Pet(name="Snowy", species="dog", photo_url="https://images.pexels.com/photos/2523934/pexels-photo-2523934.jpeg?auto=compress&cs=tinysrgb&w=1260&h=750&dpr=2", age=1, notes="Found rolling in the snow. He's a snow angel.", available=True)
pet_9 = Pet(name="Spinderella", species="porcupine", age=3, notes="More spiny than a cactus", available=True)
pet_10 = Pet(name="Mario", species="porcupine", photo_url="https://images.saymedia-content.com/.image/c_limit%2Ccs_srgb%2Cq_auto:eco%2Cw_1024/MTc0NDM2NjU2NDU4MjQ1NDgw/names-for-pet-hedgehogs-porcupines-and-tenrecs.webp", age=30, notes="They aren't that ancient", available=True)
pet_11 = Pet(name="Annabelle", species="cat", age=4, available=False)

for pet in [pet_1, pet_2, pet_3, pet_4, pet_5, pet_6, pet_7, pet_8, pet_9, pet_10, pet_11]:
    db.session.add(pet)
db.session.commit()
