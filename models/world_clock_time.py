class WorldClockTime:
    def __init__(self, days: int, hours: int, minutes: int):
        self.days = days
        self.hours = hours
        self.minutes = minutes

    def __str__(self):
        return f"{self.days}d {self.hours}h {self.minutes}m"