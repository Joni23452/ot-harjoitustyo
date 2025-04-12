import unittest
from entities.items import Item, ItemDatabase

class TestItem(unittest.TestCase):
    def setUp(self):
        self.item = Item("kala", 1)
    
    def test_get_name_returns_item_name(self):
        self.assertEqual(self.item.get_name(), "kala")

    def test_get_value_returns_correct_value(self):
        self.assertEqual(self.item.get_value(), 1)

class TestItemDatabase(unittest.TestCase):
    def setUp(self):
        self.items = ItemDatabase()
        self.items.add_item(Item("kala", 1))
        self.items.add_item(Item("kivi", 10))
    
    def test_first_item_added_is_found_at_id_0(self):
        item = self.items.get_item_by_id(0)
        self.assertEqual(item.get_name(), "kala")
    
    def test_name_to_key_returns_correct_key(self):
        key = self.items.get_item_id_by_name("kala")
        self.assertEqual(key, 0)


