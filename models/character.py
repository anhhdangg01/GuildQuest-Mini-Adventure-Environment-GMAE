from inventory import Inventory
from enums.character_class import CharacterClass
import uuid

class Character:
    def __init__(self, id: str, name: str, charClass: CharacterClass, level: int):
        self.id = id
        self.name = name
        self.charclass = charClass
        self.level = level
        self.inventory = Inventory(uuid.uuid4())

    def getInventory(self) -> Inventory:
        return self.inventory

    def rename(self, newName: str) -> None:
        self.name = newName

    def changeClass(self, newClass: CharacterClass) -> None:
        self.charClass = newClass

    def setLevel(self, newLevel: int) -> None:
        self.level = newLevel
