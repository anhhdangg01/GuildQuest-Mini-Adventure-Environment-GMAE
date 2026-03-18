# profile.py

class Profile:

    def __init__(self, character_name, preferred_realm, inventory_snapshot):
        self.characterName = character_name
        self.preferredRealm = preferred_realm
        self.inventorySnapShot = inventory_snapshot

        # Map<WorldClockTime, QuestEvent>
        self.questHistory= {}

        # List<Achievement>
        self.achievements= []

    # changePreferredRealm(Realm realm): void
    def changePreferredRealm(self, realm):
        self.preferredRealm = realm

    # changeSnapshot(): void
    def changeSnapshot(self, new_snapshot):
        self.inventorySnapShot = new_snapshot

    # updateQuestHistory(QuestEvent event): void
    def updateQuestHistory(self, event):
        time = event.startTime
        self.questHistory[time] = event

    # addAchievement(Achievement achievement): void
    def addAchievement(self, achievement):
        self.achievements.append(achievement)