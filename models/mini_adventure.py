from models.realm import Realm
from models.entity import Entity
from models.rule import Rule
from models.objective import Objective
from enums.status import Status

class MiniAdventure():
    def __init__(self, name: str, description: str, realm: Realm, status: Status):
        self.name = name
        self.description = description
        self.realm = realm
        self.quest_events = {}
        self.entities = {}
        self.rules = {}
        self.objectives = {}
        self.status = status
    
    def get_name(self) -> str:
        return self.name
    
    def get_description(self) -> str:
        return self.description

    def change_realm(self, realm: Realm) -> None:
        self.realm = realm

    def get_quest_events(self) -> dict:
        return self.quest_events
    
    def add_quest_event(self, title, quest_event) -> None:
        self.quest_events[title] = quest_event

    def remove_quest_event(self, title) -> None:
        self.quest_events.pop(title)

    def add_entity(self, entity: Entity) -> None:
        self.entities[entity.get_name()] = entity
        
    def add_rule(self, name: str, description: str="") -> None:
        self.rules[name] = Rule(name, description)

    def add_objective(self, name: str, description: str="") -> None:
        self.objectives[name] = Objective(name, description)

    def change_status(self, status: Status) -> None:
        self.status = status
