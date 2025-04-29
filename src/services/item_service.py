from repositories.item_repository import ItemRepository
from repositories.inventory_repository import default_inventory_repository
from services.random_service import RandomService

class ItemService:
    """Luokka joka toteuttaa palveluita tavaran saamiseen, muuntamiseen, sekä tietojen hakemiseen.
    """
    def __init__(self, inventory_repository=default_inventory_repository):
        """Luokan konstruktori joka alustaa palvelun.

        Args:
            inventory_repository (InventoryRepository, optional): Tavaraluettelon sekä 
              sen pysyväistalletuksen toteuttava luokka. Defaults to default_inventory_repository.
        """
        self.inventory_repository = inventory_repository
        self.item_repository = ItemRepository()
        self.random_service = RandomService(self.item_repository)

    def get_inventory_content(self) -> dict:
        """Hakee ja palauttaa tavaraluettelon sisällön.

        Returns:
            dict: Tavaraluettelon sisältö
        """
        return self.inventory_repository.get_content()

    def get_all_items(self) -> list:
        """Palauttaa kaikkia pelissä olemassaolevia tavaroita kuvaavat luvut.

        Returns:
            list: Lista tavaroita kuvaavista luvuista
        """
        return self.item_repository.get_all_item_ids()

    def get_item_name(self, item_id: int) -> str:
        """Hakee ja palauttaa tavaran nimen.

        Args:
            item_id (int): Haluttua tavaraa kuvaava luku

        Returns:
            str: Tavaran nimi
        """
        item_name = self.item_repository.get_item_name(item_id)
        return item_name

    def get_item_value(self, item_id: int) -> int:
        """Hakee ja palauttaa tavaran arvon.

        Args:
            item_id (int): Haluttua tavaraa kuvaava luku

        Returns:
            int: Tavaran arvo
        """
        item_value = self.item_repository.get_item_value(item_id)
        return item_value

    def get_item(self) -> int:
        """Lisää satunnaisen tavaran pelaajan tavaraluetteloon.

        Returns:
            int: Saatua tavaraa kuvaava luku
        """
        new_item = self.random_service.get_random_item()
        self.inventory_repository.add_item(new_item)
        return new_item

    def convert_item(self, item_name: str) -> list:
        """Muuntaa annetun tavaran toiseksi mikäli pelaaja omistaa annetun tavaran.

        Args:
            item_name (str): Muunnettavan tavaran nimi

        Returns:
            list: [Onnistuiko?, Uuden tavaran nimi, Uuden ja vanhan tavaran arvojen erotus]
        """
        if not self.item_repository.item_with_name_exists(item_name):
            return [False]
        item_id = self.item_repository.get_item_id_by_name(item_name)
        if self.inventory_repository.has_item(item_id):
            value = self.item_repository.get_item_value(item_id)
            new_item = self.random_service.convert_value(value)
            value_difference = self.item_repository.get_item_value(new_item)-value
            self.inventory_repository.remove_item(item_id)
            self.inventory_repository.add_item(new_item)
            return [True, self.item_repository.get_item_name(new_item), value_difference]
        return [False]

    def seen_item(self, item_id: int) -> bool:
        """Onko pelaaja kohdannut kyseisen tavaran?

        Args:
            item_id (int): Tavaraa kuvaava luku

        Returns:
            bool: Onko tavaraa kohdattu?
        """
        return self.inventory_repository.seen_item(item_id)
