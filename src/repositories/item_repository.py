from entities.items import Item, ItemDatabase
import json
import os

DIRNAME = os.path.dirname(__file__)
ITEMS_FILE_PATH = os.path.join(DIRNAME, "..", "data", "items.json")

class ItemRepository:
    def __init__(self):
        self._item_database = ItemDatabase()
        self._load_items(ITEMS_FILE_PATH)

    def _load_items(self, file_path):
        with open(file_path) as file:
            items: list = json.load(file)["items"]
        for item_data in items:
            name: str = item_data["name"]
            value: int = item_data["value"]
            self._add_item_to_database(name, value)

    def _add_item_to_database(self, name: str, value: int):
        item = Item(name, value)
        self._item_database.add_item(item)

    def get_item_name(self, item_id: int) -> str:
        item = self._get_item(item_id)
        return item.get_name()

    def get_item_value(self, item_id: int) -> int:
        item = self._get_item(item_id)
        return item.get_value()

    def get_all_item_ids(self) -> list:
        return self._item_database.get_ids()

    def item_with_name_exists(self, name) -> bool:
        return self._item_database.name_exists(name)

    def get_item_id_by_name(self, name) -> int:
        return self._item_database.get_item_id_by_name(name)
        
    def _get_item(self, item_id: int) -> Item:
        return self._item_database.get_item_by_id(item_id)
