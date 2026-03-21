from models.world_clock_time import WorldClockTime

class WorldClock:
    _instance = None

    def __new__(cls, *args, **kwargs):
        if not cls._instance:
            cls._instance = super(WorldClock, cls).__new__(cls)
            cls._instance._initialized = False
        return cls._instance

    def __init__(self, initial_minutes=0):
        if self._initialized:
            return
        self.total_minutes = initial_minutes
        self._initialized = True

    def advance(self, minutes: int):
        """Adds time to the world clock."""
        if minutes > 0:
            self.total_minutes += minutes

    @property
    def current_time(self) -> WorldClockTime:
        """Returns the current world time as a WorldClockTime object."""
        return WorldClockTime.from_total_minutes(self.total_minutes)

    def get_time_parts(self, absolute_minutes=None):
        """
        Converts total minutes into a (day, hour, minute) tuple.
        Uses internal time if no absolute_minutes is provided.
        """
        time_to_convert = absolute_minutes if absolute_minutes is not None else self.total_minutes
        wct = WorldClockTime.from_total_minutes(time_to_convert)
        return wct.days, wct.hours, wct.minutes

    def format_time(self, absolute_minutes=None):
        """Returns a readable string: 'Day 2, 14:30'"""
        if absolute_minutes is not None:
            return str(WorldClockTime.from_total_minutes(absolute_minutes))
        return str(self.current_time)