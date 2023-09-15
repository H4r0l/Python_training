import unittest
import json
from items import Item

class TestBasic(unittest.TestCase):
    def setUp(self):
        self.objects = []
        ##Get all the objects from the JSON:
        with open("./objects.json", "r") as file:
            self.data = json.load(file)
        ##Create instances for each Item:
        for object in self.data:
            item = Item(object.get("id"), object.get("name"), object.get("useful"))
            self.objects.append(item)

    def test_is_useful(self):
        for object in self.objects:
            self.assertEqual(object.is_useful(), "The object is useful")

    def tearDown(self):
        del(self.objects)

if __name__ == '__main__':
    unittest.main()