from models.entity import Entity
from models.realm import Realm
from enums.status import Status
from models.achievement import Achievement

class User:
    def __init__(self, id: str, username: str):
        self.id = id
        self.username = username
        self.achievements: list[Achievement] = []
        self.profile = None
        self.mAdventures = {}
        self.characters = {}

    def getMAdventures(self) -> None:
        return self.mAdventures

    def getCharacters(self) -> None:
        return self.characters

    def createMAdventure(self, name: str, MA: dict) -> None:
        if (name not in self.mAdventures):
            self.mAdventures[name] = MA
        else:
            print("> That campaign already exists!\n")

    def removeMAdventure(self, name: str) -> None:
        if (name in self.mAdventures):
            self.mAdventures.pop(name)
        else:
            print("> That campaign does not exist!\n")

    def get_quest_events(self) -> dict:
        return self.quest_events
    
    def change_realm(self, mAdventure: str, realm: Realm) -> None:
        mAdventures = self.getMAdventures()
        ma = mAdventures[mAdventure]
        ma.change_realm(realm)
    
    def add_quest_event(self, title, quest_event) -> None:
        self.quest_events[title] = quest_event

    def remove_quest_event(self, title) -> None:
        self.quest_events.pop(title)

    def add_entity(self, mAdventure: str, entity: Entity) -> None:
        mAdventures = self.getMAdventures()
        ma = mAdventures[mAdventure]
        ma.add_entity(entity)
        
    def add_rule(self, mAdventure: str, name: str, description: str="") -> None:
        mAdventures = self.getMAdventures()
        ma = mAdventures[mAdventure]
        ma.add_rule(name, description)

    def add_objective(self, mAdventure: str, name: str, description: str="") -> None:
        mAdventures = self.getMAdventures()
        ma = mAdventures[mAdventure]
        ma.add_objective(name, description)

    def change_status(self, mAdventure: str, status: Status) -> None:
        mAdventures = self.getMAdventures()
        ma = mAdventures[mAdventure]
        ma.change_status(status)

    def add_achievement(self, achievement: Achievement):
        self.achievements.append(achievement)

    def get_achievements(self):
        return self.achievements
