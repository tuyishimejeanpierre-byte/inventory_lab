from utils.json_storage import JSONStorage
from models.product import Product
from services.openfood_service import OpenFoodService


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
def update_product(self, product_id, updates):

    data = self.storage.load()

    inventory = data["inventory"]

    for product in inventory:

        if product["id"] == product_id:

            product.update(updates)

            self.storage.save(data)

            return product

    return None
def delete_product(self, product_id):

    data = self.storage.load()

    inventory = data["inventory"]

    for product in inventory:

        if product["id"] == product_id:

            inventory.remove(product)

            self.storage.save(data)

            return True
        

    return False
def import_from_openfood(self, barcode, quantity, buying_price, selling_price):

    api = OpenFoodService()

    product_data = api.search_by_barcode(barcode)

    if not product_data:
        return None

    data = self.storage.load()

    inventory = data["inventory"]

    new_product = {
        "id": self.storage.generate_id(),
        "barcode": product_data["barcode"],
        "product_name": product_data["product_name"],
        "brand": product_data["brand"],
        "quantity": quantity,
        "buying_price": buying_price,
        "selling_price": selling_price
    }

    inventory.append(new_product)

    self.storage.save(data)

    return new_product