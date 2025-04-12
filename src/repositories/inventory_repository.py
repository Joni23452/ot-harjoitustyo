from entities.inventory import Inventory
import json
import os

DIRNAME = os.path.dirname(__file__)
INVENTORY_FILE_PATH = os.path.join(DIRNAME, "..", "data", "inventory.json")

class InventoryRepository:
    def __init__(self):
        self._file_path = INVENTORY_FILE_PATH
        self._inventory = Inventory()
        self._load_inventory(self._file_path)

    def _load_inventory(self, file_path):
        with open(file_path) as file:
            inventory: dict = json.load(file)
        for item_id in inventory:
            count: int = inventory[item_id]
            self._inventory.add_items(int(item_id), count)
    
    def _write_to_file(self, file_path):
        content = self.get_content()
        with open(file_path, "w") as file:
            json.dump(content, file, indent=4)

    def add_item(self, item_id: int):
        self._inventory.add_items(item_id, 1)
        self._write_to_file(self._file_path)

    def remove_item(self, item_id: int):
        self._inventory.remove_item(item_id)
        self._write_to_file(self._file_path)
    
    def has_item(self, item_id: int) -> bool:
        return self._inventory.has_item(item_id)

    def get_content(self) -> dict:
        return self._inventory.get_content()