from inventory import Inventory
from items import Item, ItemsDatabase

inv = Inventory()
items = ItemsDatabase()
items.add_item(Item("kala",1))

while True:
    if input("Type GET to get an item: ") == "GET":
        inv.add_item(0)
    inventory_string = ""
    inventory_content = inv.get_content()
    for item_key in inventory_content:
        item = items.get_item_by_key(item_key)
        item_name = item.get_name()
        count = inventory_content[item_key]
        inventory_string+=(f"{item_name}: {count}\n")
    print(inventory_string)