from models.world_clock_time import WorldClockTime
from models.world_clock import WorldClock

class QuestEvent:
    def __init__(self, id: str, title: str, startTime: WorldClockTime, endTime: WorldClockTime = None):
        self.id = id
        self.title = title
        self.startTime = startTime
        self.endTime = endTime

    def rename(self, newTitle: str):
        self.title = newTitle

    def updateStartTime(self, newStartTime: WorldClockTime):
        self.startTime = newStartTime

    def updateEndTime(self, newEndTime: WorldClockTime):
        self.endTime = newEndTime

    def is_started(self) -> bool:
        """Returns True if the world clock has reached the event's start time."""
        return WorldClock().current_time >= self.startTime

    def is_ended(self) -> bool:
        """Returns True if the event has an end time and the world clock has reached it."""
        if not self.endTime:
            return False
        return WorldClock().current_time >= self.endTime

    def is_active(self) -> bool:
        """Returns True if the event has started but not yet ended."""
        if self.endTime:
            return self.is_started() and not self.is_ended()
        return self.is_started()
