import json
import os
from entities.inventory import Inventory

class InventoryRepository:
    def __init__(self, file_path):
        self._file_path = file_path
        self._inventory = Inventory()
        self._seen_items = []
        self._load_data(self._file_path)

    def _load_data(self, file_path):
        with open(file_path, encoding="utf-8") as file:
            data: dict = json.load(file)
        self._seen_items = data["seen_items"]
        inventory_content = data["inventory_content"]
        for item_id in inventory_content:
            count: int = inventory_content[item_id]
            self._inventory.add_items(int(item_id), count)

    def _write_to_file(self, file_path):
        content = {}
        content["inventory_content"] = self.get_content()
        content["seen_items"] = self._seen_items
        with open(file_path, "w", encoding="utf-8") as file:
            json.dump(content, file, indent=4)

    def add_item(self, item_id: int):
        self._inventory.add_items(item_id, 1)
        if item_id not in self._seen_items:
            self._seen_items.append(item_id)
        self._write_to_file(self._file_path)

    def remove_item(self, item_id: int):
        self._inventory.remove_item(item_id)
        self._write_to_file(self._file_path)

    def has_item(self, item_id: int) -> bool:
        return self._inventory.has_item(item_id)

    def get_content(self) -> dict:
        return self._inventory.get_content()

    def seen_item(self, item_id: int) -> bool:
        return item_id in self._seen_items

dirname = os.path.dirname(__file__)
inventory_default_file_path = os.path.join(dirname, "..", "data", "inventory.json")
default_inventory_repository = InventoryRepository(inventory_default_file_path)
