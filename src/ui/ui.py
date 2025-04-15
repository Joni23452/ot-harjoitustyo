from services.item_service import ItemService

COMMANDS = {
    "GET": "get an item",
    "CONVERT": "convert an item to another",
    "LIST": "lists all the items you own and their values"
}

class Ui:
    def __init__(self):
        self.item_service = ItemService()

    def start(self):
        self._print_commands()
        while True:
            command = self._get_input("Command: ")
            match command:
                case "GET": self._get_item()
                case "CONVERT": self._convert()
                case "LIST": self._print_inventory()
                case _: self._print_commands()

    def _get_input(self, message: str):
        return input(message)

    def _get_item(self):
        item = self.item_service.get_item()
        item_name = self.item_service.get_item_name(item)
        item_value = self.item_service.get_item_value(item)
        print(f"You got {item_name}, value: {item_value}")

    def _convert(self):
        item = self._get_input("Item to convert: ")
        self.item_service.convert_item(item)

    def _print_commands(self):
        print("List of commands:")
        for command in COMMANDS:
            print(f"{command} - {COMMANDS[command]}")

    def _print_inventory(self):
        inventory_string = ""
        inventory_content = self.item_service.get_inventory_content()
        total_value = 0
        for item in inventory_content:
            item_name = self.item_service.get_item_name(item)
            item_value = self.item_service.get_item_value(item)
            item_count = inventory_content[item]
            total_value += item_count*item_value
            inventory_string += f"{item_count} {item_name} (Value: {item_value}) \n"
        inventory_string += f"Total value: {total_value}"
        print(inventory_string)