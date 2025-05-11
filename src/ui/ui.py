from services.item_service import ItemService

COMMANDS = {
    "GET": "get an item",
    "CONVERT": "convert an item to another",
    "LIST": "lists all the items you own and their values",
    "ITEMS": "lists which and how many items you have found",
    "QUIT": "closes the game"
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
                case "ITEMS": self._print_found_items()
                case "QUIT": exit()
                case _: self._print_commands()

    def _get_input(self, message: str):
        return input(message)

    def _get_item(self):
        item = self.item_service.get_item()
        item_name = self.item_service.get_item_name(item)
        item_value = self.item_service.get_item_value(item)
        print(f"You got {item_name}, value: {item_value}")

    def _convert(self):
        item_name = self._get_input("Item to convert: ")
        result = self.item_service.convert_item(item_name)
        if result[0]:
            print(f"Converted {item_name} to {result[1]}. Value gain/loss: {result[2]}")
        else:
            print("Converting failed. You may have mistyped the name or you don't have the item.")

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

    def _print_found_items(self):
        items_string = ""
        items = self.item_service.get_all_items()
        total_items = len(items)
        seen_items = 0
        for item in items:
            if self.item_service.seen_item(item):
                seen_items += 1
                item_name = self.item_service.get_item_name(item)
                items_string += f"{item_name}\n"
            else:
                items_string += f"???\n"
        items_string += f"You have found {seen_items}/{total_items} items"
        print(items_string)
