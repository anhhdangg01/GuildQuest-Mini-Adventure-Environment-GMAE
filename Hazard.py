from Entity import Entity
from Enum_Classes.EntityType import EntityType

class Hazard(Entity):
    def __init__(self, name: str, type: EntityType, damage: float):
        super().__init__(name, type)
        self.damage = damage
        self.triggered = False

    def check_trigger_condition(self) -> bool:
        return True

    def trigger(self) -> None:
        self.triggered = True
    
    def untrigger(self) -> None:
        self.triggered = False
