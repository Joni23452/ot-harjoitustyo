import unittest
import os
from services.item_service import ItemService
from repositories.inventory_repository import InventoryRepository

class TestItemService(unittest.TestCase):
    def setUp(self):
        dirname = os.path.dirname(__file__)
        test_inventory_file_path = os.path.join(dirname, "..", "..", "data", "test_inventory.json")
        with open(test_inventory_file_path, "w") as file:
            file.write("{}")
        test_inventory_repository = InventoryRepository(test_inventory_file_path)
        self.item_service = ItemService(test_inventory_repository)
        
    def test_get_item_adds_an_item_to_inventory(self):
        self.item_service.get_item()
        inventory_content = self.item_service.get_inventory_content()
        items = list(inventory_content.keys())
        self.assertEqual(len(items),1)
        self.assertEqual(inventory_content[items[0]],1)

    def test_successful_convert_returns_a_different_item(self):
        self.item_service.get_item()
        items = self.item_service.get_inventory_content()
        item = list(items.keys())[0]
        item_name = self.item_service.get_item_name(item)
        result = self.item_service.convert_item(item_name)
        self.assertTrue(result[0])
        self.assertNotEqual(result[1], item_name)
