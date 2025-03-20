from inventory import Inventory

inv = Inventory()

while True:
    if input("Type GET to get an item: ") == "GET":
        inv.add_item(1)
    print(inv.get_content())