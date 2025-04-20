import unittest
import os
from services.item_service import ItemService
from repositories.inventory_repository import InventoryRepository

class TestItemService(unittest.TestCase):
    def setUp(self):
        dirname = os.path.dirname(__file__)
        test_inventory_file_path = os.path.join(dirname, "..", "..", "data", "test_inventory.json")
        with open(test_inventory_file_path, "w") as file:
            default_content = '{"inventory_content": {},"seen_items": []}'
            file.write(default_content)
        test_inventory_repository = InventoryRepository(test_inventory_file_path)
        self.item_service = ItemService(test_inventory_repository)
        
    def test_get_item_adds_an_item_to_inventory(self):
        self.item_service.get_item()
        inventory_content = self.item_service.get_inventory_content()
        items = list(inventory_content.keys())
        self.assertEqual(len(items),1)
        self.assertEqual(inventory_content[items[0]],1)

    def test_successful_convert_returns_a_different_item(self):
        item_id = self.item_service.get_item() 
        item_name = self.item_service.get_item_name(item_id)
        convert_result = self.item_service.convert_item(item_name)
        success = convert_result[0]
        self.assertTrue(success)
        new_item_name = convert_result[1]
        self.assertNotEqual(item_name, new_item_name)
    
    def test_successful_convert_changes_inventory_content(self):
        item_id = self.item_service.get_item() 
        item_name = self.item_service.get_item_name(item_id)
        inventory_before_convert = self.item_service.get_inventory_content().copy()
        convert_result = self.item_service.convert_item(item_name)
        self.assertTrue(convert_result[0])
        inventory_after_convert = self.item_service.get_inventory_content().copy()
        self.assertNotEqual(inventory_before_convert, inventory_after_convert)

    def test_failed_convert_does_not_change_inventory_content(self):
        self.item_service.get_item()
        inventory_before_convert = self.item_service.get_inventory_content().copy()
        convert_result = self.item_service.convert_item("_not_real_item")
        self.assertFalse(convert_result[0])
        inventory_after_convert =self.item_service.get_inventory_content().copy()
        self.assertEqual(inventory_before_convert, inventory_after_convert)