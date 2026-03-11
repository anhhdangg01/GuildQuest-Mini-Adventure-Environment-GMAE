from entity import Entity
from enums.entity_type import EntityType

class NPC(Entity):
    def __init__(self, name: str, type: EntityType):
        super().__init__(name, type)
        self.dialogue = {}

    def trigger_dialogue(self, dialogue: str) -> str:
        return ""
