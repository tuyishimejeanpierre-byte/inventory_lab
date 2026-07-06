import unittest
import os

from services.inventory_service import InventoryService
from utils.json_storage import JSONStorage


class TestInventoryService(unittest.TestCase):

    def setUp(self):
        self.filename = "test_db.json"
        self.storage = JSONStorage(self.filename)
        self.storage.save({"inventory": []})

        self.service = InventoryService(self.storage)

    def tearDown(self):
        if os.path.exists(self.filename):
            os.remove(self.filename)

    def test_get_inventory(self):
        inventory = self.service.get_inventory()

        self.assertEqual(inventory, [])