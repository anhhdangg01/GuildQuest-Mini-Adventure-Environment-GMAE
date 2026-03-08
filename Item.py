from Rarity import Rarity
from Type import Type

class Item:
    def __init__(self, id: str, name: str, rarity: Rarity, type: Type):
        self.id = id
        self.name = name
        self.rarity = rarity
        self.type = type

    def rename(self, newName: str) -> None:
        self.name = newName

    def setRarity(self, newRarity: Rarity) -> None:
        self.rarity = newRarity

    def setType(self, newType: Type) -> None:
        self.type = newType
