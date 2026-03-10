from NPC import NPC
from Enum_Classes.EntityType import EntityType
from Item import Item

class Vendor(NPC):
    def __init__(self, name, type: EntityType):
        super().__init__(name, type)
        self.stock = []

    def add_stock(self, item: Item) -> None:
        self.stock.append(item)

    def remove_stock(self, item: Item) -> None:
        self.stock.remove(item)

    def change_stock(self, items: list) -> None:
        self.stock = items
