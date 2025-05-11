import random
from repositories.item_repository import ItemRepository

EXPONENT = 2
# Higher exponent makes convert even less likely to return items with large value difference.
# Exponent 1 adds no exponent effect.

class RandomService:
    """Luokka jonka tehtävänä on valita satunnaisia esineitä annetun luvun perusteella
    """
    def __init__(self, item_repository: ItemRepository):
        """Luokan konstruktori joka alustaa palvelun.

        Args:
            item_repository (ItemRepository): Tieto pelissä olevista esineistä.
        """
        self.item_ids = item_repository.get_all_item_ids()
        self.values = []
        for item_id in self.item_ids:
            value = item_repository.get_item_value(item_id)
            self.values.append(value)

    def get_random_item(self):
        """Palauttaa satunnaisen esineen.

        Returns:
            int: Valittua tavaraa kuvaava luku
        """
        # Same as converting -1 value so raising to power has effect on value 1 items.
        return self.convert_value(-1)

    def convert_value(self, value):
        """Valitsee ja palauttaa satunnaisen esineen annetun luvun (tavaran arvon) perusteella.

        Args:
            value (int): Tavaran arvo tai arvoa kuvaava luku

        Returns:
            int: valittua tavaraa kuvaava luku
        """
        weights = self._form_weights(value)
        return random.choices(self.item_ids, weights)[0]

    # Items with a greater value difference to the converting value are given smaller weights
    # than items with a smaller value difference.
    def _form_weights(self, value):
        relative_values = self._relative_values(value)
        raised_relative_values = raise_to_power(relative_values, EXPONENT)
        weights = invert_values(raised_relative_values)
        return weights

    def _relative_values(self, value):
        result = []
        for i in self.values:
            result.append(abs(i-value))
        return result

def raise_to_power(values: list, exponent) -> list:
    raised = []
    for value in values:
        raised.append(value**exponent)
    return raised

def invert_values(values: list) -> list:
    inverted = []
    for value in values:
        inverted.append(inverse(value))
    return inverted

def inverse(value: int) -> int:
    if value == 0:
        return 0
    return value**-1
