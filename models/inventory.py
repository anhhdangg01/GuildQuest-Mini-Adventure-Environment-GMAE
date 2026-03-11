from item import Item

class Inventory:
    def __init__(self, id: str):
        self.id = id
        self.items = {}

    def getItems(self) -> dict:
        return self.items

    def addItem(self, name: str, item: Item) -> None:
        self.items[name] = item

    def removeItem(self, name: str) -> None:
        self.items.pop(name)
