class Profile:

    def __init__(self, character_name, preferred_realm, inventory_snapshot):
        self.characterName = character_name
        self.preferredRealm = preferred_realm
        self.inventorySnapShot = inventory_snapshot

        self.questHistory= {}

        self.achievements= []

    def changePreferredRealm(self, realm):
        self.preferredRealm = realm

    def changeSnapshot(self, new_snapshot):
        self.inventorySnapShot = new_snapshot

    def updateQuestHistory(self, event):
        time = event.startTime
        self.questHistory[time] = event

    def addAchievement(self, achievement):
        self.achievements.append(achievement)