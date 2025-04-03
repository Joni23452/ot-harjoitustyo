class Inventory:
    def __init__(self):
        self.content = {}

    def get_content(self):
        return self.content

    def add_item(self, item_key):
        if item_key in self.content:
            self.content[item_key]+=1
        else:
            self.content[item_key]=1

    def remove_item(self, item_key):
        if self.content[item_key] == 1:
            self.content.pop(item_key)
        else:
            self.content[item_key]-=1
