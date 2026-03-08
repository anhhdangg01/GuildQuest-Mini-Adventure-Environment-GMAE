class User:
    def __init__(self, id: str, username: str):
        self.id = id
        self.username = username
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
