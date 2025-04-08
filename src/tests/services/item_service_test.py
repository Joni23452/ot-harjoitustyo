import unittest
from services.item_service import ItemService

class TestItemService(unittest.TestCase):
    def setUp(self):
        self.item_service = ItemService()
        
    def test_get_item_adds_an_item_to_inventory(self):
        self.item_service.get_item()
        inventory_content = self.item_service.get_inventory_content()
        items = list(inventory_content.keys())
        self.assertEqual(len(items),1)
        self.assertEqual(inventory_content[items[0]],1)