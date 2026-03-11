from choices.choice import Choice
from choices.user_choice import UserChoice
from choices.realm_choice import RealmChoice
from choices.character_choice import CharacterChoice
from choices.quest_event_choice import QuestEventChoice
from user_data import UserData
from user import User

class ChoiceUI(Choice):
    _instance = None

    def __init__(self):
        if not self._initialized:
            self.userChoice = UserChoice()
            self.realmChoice = RealmChoice()
            self.characterChoice = CharacterChoice()
            self.questEventChoice = QuestEventChoice()
            self.userData = UserData()
            self._initialized = True

    def __new__(cls):
        if cls._instance is None:
            cls._instance = super().__new__(cls)
            cls._instance._initialized = False
        return cls._instance

    def checkUser(self, username) -> User:
        return self.userChoice.checkUser(username, self.userData.users)

    def getUserChoice(self, user) -> None:
        self.userChoice.getUserChoice(self._instance, user)

    def getRealmChoice(self) -> None:
        self.realmChoice.getRealmChoice(self.userData.realms)

    def getCharacterChoice(self, user) -> None:
        self.characterChoice.getCharacterChoice(user)

    def getQuestEventChoice(self, campaign) -> None:
        self.questEventChoice.getQuestEventChoice(campaign)
