from unittest import TestCase
from werkzeug.datastructures import MultiDict, ImmutableMultiDict

from app import app
from models import db, Pet

app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql:///adopt_test'
app.config['SQLALCHEMY_ECHO'] = False

app.config['TESTING'] = True
app.config['WTF_CSRF_ENABLED'] = False

app.config['DEBUG_TB_HOSTS'] = ['dont-show-debug-toolbar']

db.drop_all()
db.create_all()

class PetViewsTestCase(TestCase):
    """ Test Case for Pet views """

    def setUp(self):
        """ Add sample pets """

        all_pets = Pet.query.all()
        for test_pet in all_pets:
            db.session.delete(test_pet)
        pet_1 = Pet(name="Woofly", species="dog", photo_url="https://images.pexels.com/photos/4587996/pexels-photo-4587996.jpeg?auto=compress&cs=tinysrgb&w=1260&h=750&dpr=2", age=3, notes="Loves to eat waffles and run in the mud", available=True)
        pet_2 = Pet(name="Porchetta",species="porcupine", photo_url="https://images.pexels.com/photos/5030891/pexels-photo-5030891.jpeg?auto=compress&cs=tinysrgb&w=1260&h=750&dpr=2", age=2, available=False)
        pet_3 = Pet(name="Snargle", species="cat", photo_url="https://images.pexels.com/photos/991831/pexels-photo-991831.jpeg?auto=compress&cs=tinysrgb&w=1260&h=750&dpr=2", age=4, available=True)
        for pet in [pet_1, pet_2, pet_3]:
            db.session.add(pet)
        db.session.commit()
    
    def tearDown(self):
        """ Tear Down """

        db.session.rollback()
    
    def test_list_pets(self):
        with app.test_client() as client:
            resp = client.get("/")
            html = resp.get_data(as_text=True)
            self.assertEqual(resp.status_code,200)
            self.assertIn("Woofly",html)
            self.assertIn("<b>is available</b>",html)
            self.assertIn("Porchetta",html)
            self.assertIn("Snargle",html)
    
    def test_new_pet(self):
        with app.test_client() as client:
            new_pet = {
                "name": "Misty",
                "species": "cat",
                "photo_url": "https://images.pexels.com/photos/3687957/pexels-photo-3687957.jpeg?auto=compress&cs=tinysrgb&h=750&w=1260",
                "age": 14,
                "notes": "A bit camera shy",
                "available": "false"
            }
            resp = client.post('/add', data=new_pet, follow_redirects=True)
            html = resp.get_data(as_text=True)
            self.assertEqual(resp.status_code,200)
            self.assertIn("Misty",html)
            self.assertNotIn("Misty <b>is available</b>",html)
        with app.test_client() as client:
            new_pet  = Pet.query.filter_by(name="Misty").first()
            resp = client.get(f'/{new_pet.id}')
            html = resp.get_data(as_text=True)
            self.assertEqual(resp.status_code,200)
            self.assertNotIn("Available!",html)
            self.assertIn("Age: 14",html)
            self.assertIn("A bit camera shy",html)
            self.assertIn("Species: Cat",html)
            self.assertIn("https://images.pexels.com/photos/3687957/pexels-photo-3687957",html)
    
    def test_edit_pet(self):
        with app.test_client() as client:
            pet_to_edit = Pet.query.filter_by(name="Porchetta").one()
            edited_pet = {
                "photo_url": "",
                "notes": "More spiny than a cactus",
                "available": "false"
            }
            resp = client.post(f'/{pet_to_edit.id}/edit', data=edited_pet, follow_redirects=True)
            html = resp.get_data(as_text=True)
            self.assertEqual(resp.status_code,200)
            self.assertIn("More spiny than a cactus",html)
            self.assertNotIn("Available!",html)
            self.assertNotIn("<img",html)