import unittest
from entities.items import Item

class TestItem(unittest.TestCase):
    def setUp(self):
        self.item = Item("kala", 1)
    
    def test_get_name_returns_item_name(self):
        self.assertEqual(self.item.get_name(), "kala")


