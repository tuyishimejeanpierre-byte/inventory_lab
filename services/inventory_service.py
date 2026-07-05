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
    
    def add_product(
    self,
    barcode,
    product_name,
    brand,
    quantity,
    buying_price,
    selling_price
):
        
        data = self.storage.load()


        inventory = data["inventory"]


        product = Product(
        product_id=self.storage.generate_id(),
        barcode=barcode,
        product_name=product_name,
        brand=brand,
        quantity=quantity,
        buying_price=buying_price,
        selling_price=selling_price
     )

        inventory.append(product.to_dict())

        self.storage.save(data)

        return product.to_dict()