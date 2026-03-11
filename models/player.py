from entity import Entity
from item import Item
from vendor import Vendor

class Player(Entity):
    def __init__(self):
        self.money = 0.0
        self.actions = {}

    def sell(self, item: Item, vendor: Vendor) -> None:
        pass
    
    def purchase(self, item: Item, vendor: Vendor) -> None:
        pass

    def act(self) -> None:
        pass