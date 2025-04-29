class Inventory:
    """Luokka jonka avulla ylläpidetään pelaajan tavaraluetteloa.

    Attributes:
        content: Dictionary tavaraluettelon sisällöstä.    
    """
    def __init__(self):
        """Luokan konstruktori joka luo tyhjän tavaraluettelon.
        """
        self.content = {}

    def get_content(self) -> dict:
        """Palauttaa tavaraluettelon sisällön.

        Returns:
            dict: Tavaraluettelon sisältö.
        """
        return self.content

    def has_item(self, item_id: int) -> bool:
        """Palauttaa sisältääkö tavaraluettelo tietyn tavaran.

        Args:
            item_id (int): Tavaraa kuvaava luku

        Returns:
            bool: Sisältääkö tavaran
        """
        return item_id in self.content

    def add_items(self, item_id: int, count: int):
        """Lisää tavaraa tavaraluetteloon.

        Args:
            item_id (int): Tavaraa kuvaava luku
            count (int): Määrä
        """
        if item_id in self.content:
            self.content[item_id]+=count
        else:
            self.content[item_id]=count

    def remove_item(self, item_id: int):
        """Poistaa tavaran tavaraluettelosta.

        Args:
            item_id (int): Tavaraa kuvaava luku
        """
        if self.content[item_id] == 1:
            self.content.pop(item_id)
        else:
            self.content[item_id]-=1
