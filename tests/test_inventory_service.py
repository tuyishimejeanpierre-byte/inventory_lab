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

from services.inventory_service import InventoryService
from utils.json_storage import JSONStorage


def test_add_product():
    storage = JSONStorage("test_db.json")
    storage.save({"inventory": []})

    service = InventoryService(storage)

    product = service.add_product(
        barcode="123456789",
        product_name="Test Milk",
        brand="DairyBest",
        quantity=10,
        buying_price=50,
        selling_price=70
    )

    assert product is not None
    assert product["product_name"] == "Test Milk"
    assert product["brand"] == "DairyBest"
    assert product["quantity"] == 10