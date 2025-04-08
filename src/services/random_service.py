import random
from entities.items import Item, ItemsDatabase

class RandomService:
    def __init__(self, items:ItemsDatabase):
        self.item_keys = list(items.get_keys())
        self.values = []
        for item_key in self.item_keys:
            item:Item = items.get_item_by_key(item_key)
            value = item.get_value()
            self.values.append(value)

    def convert(self, value):
        weights = self._form_weights(value)
        return random.choices(self.item_keys, weights)[0]

    def _form_weights(self, value):
        relative_values = self._relative_values(value)
        weights = invert_values(relative_values)
        return weights

    def _relative_values(self, value):
        result = []
        for i in self.values:
            result.append(abs(i-value))
        return result

def invert_values(values:list):
    inverted = []
    for value in values:
        inverted.append(inverse(value))
    return inverted

def inverse(value:int):
    if value == 0:
        return 0
    return value**-1
