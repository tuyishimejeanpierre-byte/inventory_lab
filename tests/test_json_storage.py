import unittest
import os

from utils.json_storage import JSONStorage


class TestJSONStorage(unittest.TestCase):

    def setUp(self):
        self.filename = "test_db.json"
        self.storage = JSONStorage(self.filename)

        self.storage.save({"inventory": []})

    def tearDown(self):
        if os.path.exists(self.filename):
            os.remove(self.filename)

    def test_load_empty_inventory(self):
        data = self.storage.load()
        self.assertEqual(data, {"inventory": []})

    def test_save_inventory(self):
        inventory = {
            "inventory": [
                {"id": 1, "product_name": "Milk"}
            ]
        }

        self.storage.save(inventory)

        loaded = self.storage.load()

        self.assertEqual(loaded, inventory)


if __name__ == "__main__":
    unittest.main()