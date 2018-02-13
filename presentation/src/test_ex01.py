from unittest import TestCase
from myapp.models import Animal

class AnimalTestCase(TestCase):
    def setUp(self):
        self.lion = Animal(name="lion", sound="roar")
        self.cat = Animal(name="cat", sound="meow")

    def test_animals_can_speak(self):
        """Animals that can speak are correctly identified"""
        self.assertEqual(self.lion.speak(), 'The lion says "roar"')
        self.assertEqual(self.cat.speak(), 'The cat says "meow"')