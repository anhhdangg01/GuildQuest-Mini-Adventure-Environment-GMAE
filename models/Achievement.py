from models.world_clock_time import WorldClockTime

class Achievement:
    def __init__(self, name: str, description: str, time_unlocked: WorldClockTime):
        self.name = name
        self.description = description
        self.timeUnlocked = time_unlocked

    def getName(self) -> str:
        return self.name

    def getTimeUnlocked(self) -> WorldClockTime:
        return self.timeUnlocked

    def getDescription(self) -> str:
        return self.description