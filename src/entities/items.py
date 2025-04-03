class Item:
    def __init__(self, name: str, value: int):
        self.name = name
        self.value = value

    def get_name(self):
        return self.name

class ItemsDatabase:
    def __init__(self):
        self.items = {}
        self.next_key = 0

    def add_item(self, item: Item):
        self.items[self.next_key] = item
        self.next_key += 1

    def get_item_by_key(self, item_key):
        return self.items[item_key]
