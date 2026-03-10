from Entity import Entity
from Enum_Classes.EntityType import EntityType

class NPC(Entity):
    def __init__(self, name: str, type: EntityType):
        super().__init__(name, type)
        self.dialogue = {}

    def trigger_dialogue(self, dialogue: str) -> str:
        return ""
