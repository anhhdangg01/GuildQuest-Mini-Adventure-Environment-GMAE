from WorldClockTime import WorldClockTime

class QuestEvent:
    def __init__(self, id: str, title: str, startTime: WorldClockTime, endTime:WorldClockTime=None):
        self.id = id
        self.title = title
        self.startTime = startTime
        self.endTime = endTime

    @classmethod
    def rename(self, newTitle: str):
        self.title = newTitle

    @classmethod
    def updateStartTime(self, newStartTime: WorldClockTime):
        self.startTime = newStartTime

    @classmethod
    def updateEndTime(self, newEndTime: WorldClockTime):
        self.endTime = newEndTime
