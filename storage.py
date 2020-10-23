import json
import os.path


class Storage:
    data = {}

    def __init__(self, name):
        self.name = name

    def add(self, key, value):
        self.data[key] = value

    def get(self, key):
        return self.data[key]

    def delete(self, key):
        self.data.pop(key)

    def save(self):
        with open(f"{self.name}.json", "w") as write_file:
            json.dump(self.data, write_file)

    def load(self):
        if not os.path.exists(f"{self.name}.json"):
            self.save()
        with open(f"{self.name}.json", "r") as read_file:
            self.data = json.load(read_file)

    def change_storage(self, name):
        new_storage = Storage(name)
        new_storage.load()
        self.name = name
        self.data = new_storage.data
