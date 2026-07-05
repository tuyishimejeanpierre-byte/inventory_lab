from utils.json_storage import JSONStorage
from models.product import Product


class InventoryService:

    def __init__(self):
        self.storage = JSONStorage("db.json")

    def get_inventory(self):
        return self.storage.load()["inventory"]

    def get_product(self, product_id):

        inventory = self.storage.load()["inventory"]

        for product in inventory:
            if product["id"] == product_id:
                return product

        return None