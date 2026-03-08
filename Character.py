from Inventory import Inventory
from Class import Class
import uuid

class Character:
    def __init__(self, id: str, name: str, charClass: Class, level: int):
        self.id = id
        self.name = name
        self.charclass = charClass
        self.level = level
        self.inventory = Inventory(uuid.uuid4())

    def getInventory(self) -> Inventory:
        return self.inventory

    def rename(self, newName: str) -> None:
        self.name = newName

    def changeClass(self, newClass: Class) -> None:
        self.charClass = newClass

    def setLevel(self, newLevel: int) -> None:
        self.level = newLevel
