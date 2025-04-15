from repositories.item_repository import ItemRepository
from repositories.inventory_repository import InventoryRepository
from services.random_service import RandomService

class ItemService:
    def __init__(self):
        self.inventory_repository = InventoryRepository()
        self.item_repository = ItemRepository()
        self.random_service = RandomService(self.item_repository)

    def get_inventory_content(self):
        return self.inventory_repository.get_content()

    def get_item_name(self, item_id):
        item_name = self.item_repository.get_item_name(item_id)
        return item_name

    def get_item_value(self, item_id):
        item_value = self.item_repository.get_item_value(item_id)
        return item_value

    def get_item(self):
        new_item = self.random_service.convert(0)
        self.inventory_repository.add_item(new_item)

    def convert_item(self, item_name):
        item_id = self.item_repository.get_item_id_by_name(item_name)
        if self.inventory_repository.has_item(item_id):
            value = self.item_repository.get_item_value(item_id)
            new_item = self.random_service.convert(value)
            self.inventory_repository.remove_item(item_id)
            self.inventory_repository.add_item(new_item)
