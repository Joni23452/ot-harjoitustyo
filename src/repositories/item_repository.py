from entities.items import Item, ItemsDatabase

class ItemRepository:
    def __init__(self):
        self.items = ItemsDatabase()
        self._load_items()

    def _load_items(self):
        self.items.add_item(Item("kala",1))
        self.items.add_item(Item("kivi",10))
        self.items.add_item(Item("talo",100))
        self.items.add_item(Item("ötökkä",2))

    def get_item_name(self, item_id: int) -> str:
        item = self._get_item(item_id)
        return item.get_name()

    def get_item_value(self, item_id: int) -> int:
        item = self._get_item(item_id)
        return item.get_value()

    def get_all_item_ids(self) -> list:
        self.items.get_keys()

    def get_item_id_by_name(self, name) -> int:
        return self.items.get_item_key_by_name(name)
        
    def _get_item(self, item_id: int) -> Item:
        return self.items.get_item_by_key(item_id)
