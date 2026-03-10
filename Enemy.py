from NPC import NPC
from Enum_Classes.EntityType import EntityType

class Enemy(NPC):
    def __init__(self, name: str, type: EntityType):
        super().__init__(name, type)
        self.health_points = 100.0
        self.actions = []

    def act(self) -> None:
        pass
