class Inventory:
    def __init__(self):
        self.content = {}
    
    def get_content(self):
        return self.content

    def add_item(self, item):
        if item in self.content.keys():
            self.content[item]+=1
        else:
            self.content[item]=1
    
    def remove_item(self, item):
        if self.content[item] == 1:
            self.content.pop(item)
        else:
            self.content[item]-=1
