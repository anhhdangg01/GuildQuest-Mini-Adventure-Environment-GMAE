from enums.rarity import Rarity
from enums.type import Type
from models.entity import Entity
from enums.entity_type import EntityType

class Item(Entity):
    def __init__(self, id: str, name: str, entity_type: EntityType, rarity: Rarity, type: Type):
        super().__init__(name, entity_type)
        self.id = id
        self.rarity = rarity
        self.type = type

    def rename(self, newName: str) -> None:
        self.name = newName

    def setRarity(self, newRarity: Rarity) -> None:
        self.rarity = newRarity

    def setType(self, newType: Type) -> None:
        self.type = newType
