class Product:

    def __init__(
        self,
        product_id,
        barcode,
        product_name,
        brand,
        quantity,
        buying_price,
        selling_price
    ):

        self.id = product_id
        self.barcode = barcode
        self.product_name = product_name
        self.brand = brand
        self.quantity = quantity
        self.buying_price = buying_price
        self.selling_price = selling_price

    def to_dict(self):

        return {
            "id": self.id,
            "barcode": self.barcode,
            "product_name": self.product_name,
            "brand": self.brand,
            "quantity": self.quantity,
            "buying_price": self.buying_price,
            "selling_price": self.selling_price
        }