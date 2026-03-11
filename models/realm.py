from map_identity import MapIdentity

class Realm:
    def __init__(self, id: str, name: str, mapIdentity: MapIdentity, description: str = "", local_time_offset: int = 0):
        self.id = id
        self.name = name
        self.mapIdentity = mapIdentity
        self.description = description
        self.local_time_offset = local_time_offset

    def updateMapIdentity(self, x, y):
        self.mapIdentity = MapIdentity(id, x, y)

    def to_local_time(self, world_minutes):
        """
        Requirement 6: Converts World Clock time to Realm-local time.
        Formula: (WorldTime * Multiplier) + Offset
        """
        return int(world_minutes + self.local_time_offset)

    def display_event_time(self, world_minutes):
        """
        Helper to format the time using the WorldClock's formatting logic 
        but with the Realm's local calculation.
        """
        from models.world_clock import WorldClock
        clock = WorldClock()
        local_total = self.to_local_time(world_minutes)
        return clock.format_time(local_total)
