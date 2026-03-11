from choices.choice import Choice
from realm import Realm
from map_identity import MapIdentity
import uuid

class RealmChoice(Choice):
    ADD_REALM = 1
    RETURN = 2

    @staticmethod
    def printRealmChoices() -> None:
        print("> What would you like to do with your realms? Type the number:")
        print("* (1) Add realm")
        print("* (2) Return")

    @staticmethod
    def getRealmChoice(realms: dict) -> None:
        RealmChoice.printRealmChoices()
        choice = Choice.getStringInput()

        try:
            while (int(choice) != RealmChoice.RETURN):
                match (int(choice)):
                    case RealmChoice.ADD_REALM:
                        RealmChoice.addRealm(realms)
                    case RealmChoice.RETURN:
                        pass
                    case _:
                        print("> Invalid input! Try again!\n")

                RealmChoice.printRealmChoices()
                choice = Choice.getStringInput()
        except ValueError:
            print("> Your input is not a number!\n")

    @staticmethod
    def addRealm(realms: dict) -> None:
        try:
            print("> What would you like your realm's name to be?")
            name = Choice.getStringInput()

            if (name in realms):
                print("> That realm already exists!")
                return

            print("> Where would you like to be located currently in the world?")
            print("Type in your x-coordinate: ")
            x = Choice.getDoubleInput()

            print("Type in your y-coordinate: ")
            y = Choice.getDoubleInput()

            newRealm = Realm(uuid.uuid4(), name,
                        MapIdentity(uuid.uuid4(), x, y))
            realms[name] = newRealm

            print("> Realm added!\n")
        except ValueError:
            print("> Your input is not a number!\n")
