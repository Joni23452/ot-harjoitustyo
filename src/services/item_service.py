from repositories.item_repository import ItemRepository
from repositories.inventory_repository import default_inventory_repository
from services.random_service import RandomService

class ItemService:
    def __init__(self, inventory_repository=default_inventory_repository):
        self.inventory_repository = inventory_repository
        self.item_repository = ItemRepository()
        self.random_service = RandomService(self.item_repository)

    def get_inventory_content(self):
        return self.inventory_repository.get_content()
    
    def get_all_items(self):
        return self.item_repository.get_all_item_ids()

    def get_item_name(self, item_id):
        item_name = self.item_repository.get_item_name(item_id)
        return item_name

    def get_item_value(self, item_id):
        item_value = self.item_repository.get_item_value(item_id)
        return item_value

    def get_item(self):
        new_item = self.random_service.get_random_item()
        self.inventory_repository.add_item(new_item)
        return new_item

    def convert_item(self, item_name):
        if not self.item_repository.item_with_name_exists(item_name):
            return [False]
        item_id = self.item_repository.get_item_id_by_name(item_name)
        if self.inventory_repository.has_item(item_id):
            value = self.item_repository.get_item_value(item_id)
            new_item = self.random_service.convert_value(value)
            value_difference = self.item_repository.get_item_value(new_item)-value
            self.inventory_repository.remove_item(item_id)
            self.inventory_repository.add_item(new_item)
            return [True, self.item_repository.get_item_name(new_item), value_difference]
        return [False]

    def seen_item(self, item_id):
        return self.inventory_repository.seen_item(item_id)
