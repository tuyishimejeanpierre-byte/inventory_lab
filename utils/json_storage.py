import json
import os


class JSONStorage:
    def __init__(self, filename):
        self.filename = filename

    def load(self):
        if not os.path.exists(self.filename):
            return {"inventory": []}

        with open(self.filename, "r") as file:
            return json.load(file)

    def save(self, data):
        with open(self.filename, "w") as file:
            json.dump(data, file, indent=4)

    def generate_id(self):
        data = self.load()

        inventory = data["inventory"]

        if not inventory:
            return 1

        return max(item["id"] for item in inventory) + 1