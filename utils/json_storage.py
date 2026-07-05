import json


class JSONStorage:

    def __init__(self, filename):

        self.filename = filename

    def load(self):

        with open(self.filename, "r") as file:
            return json.load(file)

    def save(self, data):

        with open(self.filename, "w") as file:
            json.dump(data, file, indent=4)