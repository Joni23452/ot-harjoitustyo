from entities.items import Item, ItemsDatabase
from entities.inventory import Inventory
from services.random_service import RandomService

class ItemService:
    def __init__(self):
        self.inventory = Inventory()
        self.items = ItemsDatabase()
        self.items.add_item(Item("kala",1))
        self.items.add_item(Item("kivi",10))
        self.items.add_item(Item("talo",100))
        self.items.add_item(Item("ötökkä",2))
        self.random_service = RandomService(self.items)

    def get_inventory_content(self):
        return self.inventory.get_content()

    def get_item_name(self, item_key):
        item:Item = self.items.get_item_by_key(item_key)
        item_name = item.get_name()
        return item_name

    def get_item(self):
        self.inventory.add_item(0)

    def convert_item(self, item_name):
        item_key = self.items.get_item_key_by_name(item_name)
        if self.inventory.has_item(item_key):
            item:Item = self.items.get_item_by_key(item_key)
            value = item.get_value()
            new_item = self.random_service.convert(value)
            self.inventory.remove_item(item_key)
            self.inventory.add_item(new_item)
