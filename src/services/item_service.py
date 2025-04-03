from entities.items import Item, ItemsDatabase
from entities.inventory import Inventory

class ItemService:
    def __init__(self):
        self.inventory = Inventory()
        self.items = ItemsDatabase()
        self.items.add_item(Item("kala",1))

    def get_inventory_content(self):
        return self.inventory.get_content()

    def get_item_name(self, item_key):
        item:Item = self.items.get_item_by_key(item_key)
        item_name = item.get_name()
        return item_name

    def get_item(self):
        self.inventory.add_item(0)
