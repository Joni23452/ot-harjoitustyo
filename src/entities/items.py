class Item:
    """Luokka joka kuvastaa sisältää tiedot yksittäisestä tavarasta
    """
    def __init__(self, name: str, value: int):
        """Luokan konstruktori joka luo uuden tavaran.

        Args:
            name (str): Tavaran nimi
            value (int): Tavaran arvo
        """
        self.name = name
        self.value = value

    def get_name(self):
        """Palauttaa tavaran nimen

        Returns:
            str: Tavaran nimi
        """
        return self.name

    def get_value(self):
        """Palauttaa tavaran arvon

        Returns:
            int: Tavaran arvo
        """
        return self.value

class ItemDatabase:
    """Luokka joka ylläpitää tietoa pelin tavaroista.
    """
    def __init__(self):
        """Luokan konstruktori joka luo tyhjän kannan
        """
        self.items = {}
        self.item_name_to_id = {}
        self.next_id = 0

    def add_item(self, item: Item):
        """Lisää tavaran kantaan

        Args:
            item (Item): Tavara
        """
        self.items[self.next_id] = item
        self.item_name_to_id[item.get_name()] = self.next_id
        self.next_id += 1

    def get_item_by_id(self, item_id: int) -> Item:
        """Palauttaa tavaran sitä kuvaavan luvun perusteella

        Args:
            item_id (int): Haluttua tavaraa kuvaava luku

        Returns:
            Item: Haettu tavara
        """
        return self.items[item_id]

    def get_item_id_by_name(self, item_name: str) -> int:
        """Palauttaa tavaran sen nimen perusteella

        Args:
            item_name (str): Halutun tavaran nimi

        Returns:
            int: Haettu tavara
        """
        return self.item_name_to_id[item_name]

    def get_ids(self) -> list:
        """Palauttaa listan kantaan lisättyjä tavaroita kuvaavista luvuista.

        Returns:
            list: Lista tavaroita kuvaavista luvuista
        """
        return list(self.items.keys())

    def name_exists(self, name) -> bool:
        """Tarkistaa onko tietyn nimistä tavaraa olemassa.

        Args:
            name (str): Tavaran nimi

        Returns:
            bool: Onko kyseisen nimistä tavaraa olemassa.
        """
        return name in self.item_name_to_id
