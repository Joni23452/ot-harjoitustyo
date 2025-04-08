class Item:
    def __init__(self, name: str, value: int):
        self.name = name
        self.value = value

    def get_name(self):
        return self.name

    def get_value(self):
        return self.value

class ItemsDatabase:
    def __init__(self):
        self.items = {}
        self.item_name_to_key = {}
        self.next_key = 0

    def add_item(self, item: Item):
        self.items[self.next_key] = item
        self.item_name_to_key[item.get_name()] = self.next_key
        self.next_key += 1

    def get_item_by_key(self, item_key):
        return self.items[item_key]

    def get_item_by_name(self, item_name):
        key = self.item_name_to_key[item_name]
        return self.get_item_by_key(key)