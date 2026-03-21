class WorldClockTime:
    def __init__(self, days: int, hours: int, minutes: int):
        self.days = days
        self.hours = hours
        self.minutes = minutes

    @property
    def total_minutes(self) -> int:
        """Returns the total minutes represented by this time object."""
        return (self.days * 24 * 60) + (self.hours * 60) + self.minutes

    @classmethod
    def from_total_minutes(cls, total_minutes: int) -> WorldClockTime:
        """Creates a WorldClockTime instance from total minutes."""
        days = total_minutes // (24 * 60)
        remaining = total_minutes % (24 * 60)
        hours = remaining // 60
        minutes = remaining % 60
        return cls(days, hours, minutes)

    def __str__(self):
        return f"Day {self.days}, {self.hours:02d}:{self.minutes:02d}"

    def __eq__(self, other):
        if not isinstance(other, WorldClockTime):
            return False
        return self.total_minutes == other.total_minutes

    def __lt__(self, other):
        if not isinstance(other, WorldClockTime):
            raise TypeError("Cannot compare WorldClockTime with other types")
        return self.total_minutes < other.total_minutes

    def __le__(self, other):
        return self < other or self == other

    def __gt__(self, other):
        return not self <= other

    def __ge__(self, other):
        return not self < other