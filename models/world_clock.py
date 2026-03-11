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
        self.day, self.hour, self.minute = self.get_time_parts(initial_minutes)
        self._initialized = True

    def advance(self, minutes):
        """Adds time to the world clock."""
        if minutes > 0:
            self.total_minutes += minutes
            self.day, self.hour, self.minute = self.get_time_parts(self.total_minutes)

    def get_time_parts(self, absolute_minutes=None):
        """
        Converts total minutes into a (day, hour, minute) tuple.
        Uses internal time if no absolute_minutes is provided.
        """
        time = absolute_minutes if absolute_minutes is not None else self.total_minutes
        
        day = time // (24 * 60)
        remaining_minutes = time % (24 * 60)
        hour = remaining_minutes // 60
        minute = remaining_minutes % 60

        return day, hour, minute

    def format_time(self, absolute_minutes=None):
        """Returns a readable string: 'Day 2, 14:30'"""
        d, h, m = self.get_time_parts(absolute_minutes)
        return f"Day {d}, {h:02d}:{m:02d}"