from utils.json_storage import JSONStorage


class InventoryService:

    def __init__(self):

        self.storage = JSONStorage("db.json")

    def get_inventory(self):

        return self.storage.load()["inventory"]