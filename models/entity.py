from enums.entity_type import EntityType

class Entity():
    def __init__(self, name: str, type: EntityType):
        self.name = name
        self.type = type

    def get_name(self) -> str:
        return self.name
    
    def get_type(self) -> EntityType:
        return self.type
