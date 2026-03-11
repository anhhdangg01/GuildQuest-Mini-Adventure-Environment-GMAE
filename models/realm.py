from map_identity import MapIdentity

class Realm:
    def __init__(self, id: str, name: str, mapIdentity: MapIdentity, description:str=""):
        self.id = id
        self.name = name
        self.mapIdentity = mapIdentity
        self.description = description

    def updateMapIdentity(self, x, y):
        self.mapIdentity = MapIdentity(id, x, y)

    # @Override
    # public LocalTime toLocal(WorldClockTime world) {
    #     return null;
    # }

    # @Override
    # public WorldClockTime toWorld(LocalTime local) {
    #     return null;
    # }
