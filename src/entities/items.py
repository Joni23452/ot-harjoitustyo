class Item:
    def __init__(self, name: str, value: int):
        self.name = name
        self.value = value

    def get_name(self):
        return self.name

    def get_value(self):
        return self.value

class ItemDatabase:
    def __init__(self):
        self.items = {}
        self.item_name_to_id = {}
        self.next_id = 0

    def add_item(self, item: Item):
        self.items[self.next_id] = item
        self.item_name_to_id[item.get_name()] = self.next_id
        self.next_id += 1

    def get_item_by_id(self, item_id: int) -> Item:
        return self.items[item_id]

    def get_item_id_by_name(self, item_name: str) -> int:
        return self.item_name_to_id[item_name]

    def get_ids(self) -> list:
        return list(self.items.keys())
