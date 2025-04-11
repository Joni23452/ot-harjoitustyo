from repositories.item_repository import ItemRepository
from entities.inventory import Inventory
from services.random_service import RandomService

class ItemService:
    def __init__(self):
        self.inventory = Inventory()
        self.item_repository = ItemRepository()
        self.random_service = RandomService(self.item_repository)

    def get_inventory_content(self):
        return self.inventory.get_content()

    def get_item_name(self, item_id):
        item_name = self.item_repository.get_item_name(item_id)
        return item_name

    def get_item(self):
        new_item = self.random_service.convert(0)
        self.inventory.add_item(new_item)

    def convert_item(self, item_name):
        item_id = self.item_repository.get_item_id_by_name(item_name)
        if self.inventory.has_item(item_id):
            value = self.item_repository.get_item_value(item_id)
            new_item = self.random_service.convert(value)
            self.inventory.remove_item(item_id)
            self.inventory.add_item(new_item)
