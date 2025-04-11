import random
from repositories.item_repository import ItemRepository

class RandomService:
    def __init__(self, item_repository: ItemRepository):
        self.item_ids = item_repository.get_all_item_ids()
        self.values = []
        for item_id in self.item_ids:
            value = item_repository.get_item_value(item_id)
            self.values.append(value)

    def convert(self, value):
        weights = self._form_weights(value)
        return random.choices(self.item_ids, weights)[0]

    def _form_weights(self, value):
        relative_values = self._relative_values(value)
        weights = invert_values(relative_values)
        return weights

    def _relative_values(self, value):
        result = []
        for i in self.values:
            result.append(abs(i-value))
        return result

def invert_values(values: list) -> list:
    inverted = []
    for value in values:
        inverted.append(inverse(value))
    return inverted

def inverse(value: int) -> int:
    if value == 0:
        return 0
    return value**-1
