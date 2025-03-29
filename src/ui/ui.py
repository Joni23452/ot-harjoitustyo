from services.item_service import ItemService

class Ui:
    def __init__(self):
        self.item_service = ItemService()

    def start(self):
        while True:
            user_input = self.get_input()
            if user_input == "GET":
                self.item_service.get_item()
            self.print_inventory()

    def get_input(self):
        return input("Type GET to get an item: ")
    
    def print_inventory(self):
        inventory_string = ""
        inventory_content = self.item_service.get_inventory_content()
        for item in inventory_content:
            item_name = self.item_service.get_item_name(item)
            item_count = inventory_content[item]
            inventory_string+=(f"{item_name}: {item_count}\n")
        print(inventory_string)