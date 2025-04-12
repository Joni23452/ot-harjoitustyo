class Inventory:
    def __init__(self):
        self.content = {}

    def get_content(self) -> dict:
        return self.content

    def has_item(self, item_id: int) -> bool:
        return item_id in self.content

    def add_item(self, item_id: int):
        if item_id in self.content:
            self.content[item_id]+=1
        else:
            self.content[item_id]=1

    def remove_item(self, item_id: int):
        if self.content[item_id] == 1:
            self.content.pop(item_id)
        else:
            self.content[item_id]-=1
