from choices.choice import Choice
from models.user import User
from adventures.mini_adventure import MiniAdventure
from adventures.relic_hunt_adventure import RelicHuntAdventure
from adventures.escort_adventure import EscortAdventure
from enums.status import Status

class MAdventureChoice(Choice):
    ADD_MADVENTURE = 1
    REMOVE_MADVENTURE = 2
    JOIN_MADVENTURE = 3
    QUEST_EVENTS = 4
    RETURN = 5

    NPC = 1
    ITEM = 2
    HAZARD = 3

    WIN = 1
    LOSE = 2
    PROGRESSING = 3
    COMPLETE = 4

    GENERIC_MADVENTURE = 1
    RELIC_HUNT = 2
    ROYAL_ESCORT = 3

    COMPETITIVE = 1
    COOP = 2

    @staticmethod
    def name_in_madventures(name: str, mAdventures: dict) -> bool:
        if (name not in mAdventures):
            return False
        return True

    @staticmethod
    def print_madventure_choices() -> None:
        print("> What would you like to do with mini-adventures? Type the number of one of the following:")
        print("* (1) Add mini-adventure")
        print("* (2) Remove mini-adventure")
        print("* (3) Join mini-adventure")
        print("* (4) Quest events")
        print("* (5) Return")

    @staticmethod
    def print_madventure_type_choices() -> None:
        print("> What kind of mini-adventure do you want to create?")
        print("* (1) Generic mini-adventure")
        print("* (2) Relic Hunt")
        print("* (3) Royal Escort")

    @staticmethod
    def print_relic_hunt_mode_choices() -> None:
        print("> What mode do you want for Relic Hunt?")
        print("* (1) Competitive")
        print("* (2) Co-op")

    @staticmethod
    def print_mini_adventures(choiceUI) -> None:
        mAdventures = choiceUI.userData.mAdventures
        counter = 1
        
        print("\n=== GuildQuest Mini-Adventure Menu ===")
        if (not mAdventures):
            print("There are currently no mini-adventures.")

        for name, adventure in mAdventures.items():
            print(name, adventure)
            print(f"({counter}) {name} - {adventure.get_description()}")
            counter += 1
        print("======================================")

    @staticmethod
    def get_madventure_choice(choiceUI, user: User) -> None:
        MAdventureChoice.print_madventure_choices()
        choice = Choice.getStringInput()
        
        try:
            while(int(choice) != MAdventureChoice.RETURN):
                match (int(choice)):
                    case MAdventureChoice.ADD_MADVENTURE:
                        mAdventures = choiceUI.userData.mAdventures
                        realms = choiceUI.userData.realms
                        MAdventureChoice.add_madventure(mAdventures, realms, user)
                    case MAdventureChoice.REMOVE_MADVENTURE:
                        mAdventures = choiceUI.userData.mAdventures
                        MAdventureChoice.remove_madventure(mAdventures, user)
                    case MAdventureChoice.JOIN_MADVENTURE:
                        MAdventureChoice.play_madventure(choiceUI, user)
                    case MAdventureChoice.QUEST_EVENTS:
                        print("> Type an existing mini-adventure:")
                        mAdventure = Choice.getStringInput()

                        if (mAdventure in user.getMAdventures()):
                            choiceUI.getQuestEventChoice(user.getMAdventures()[mAdventure])
                        else:
                            print(">That mini-adventure does not exist!\n")
                    case _:
                        print("> Invalid input! Try again!\n")

                MAdventureChoice.print_madventure_choices()
                choice = Choice.getStringInput()
        except ValueError:
            print("> Your input is not a number!\n")

    @staticmethod
    def add_madventure(mAdventures: dict, realms: dict, user: User) -> None:
        print("> Please enter your mini-adventure name:")
        name = Choice.getStringInput()

        if (MAdventureChoice.name_in_madventures(name, user.getMAdventures())):
            print("> That mini-adventure already exists!\n")
            return
        
        print("> Please enter a description (press enter if you want it blank):")
        description = Choice.getStringInput()
        
        print("> Please choose the realm you want your mini-adventure to take place in: ")

        realm_str = Choice.getStringInput()
        if (realm_str not in realms):
            print("> That realm does not exist!\n")
            return
        
        realm = realms[realm_str]

        MAdventureChoice.print_madventure_type_choices()
        madventure_type = Choice.getIntInput()

        if (madventure_type == MAdventureChoice.GENERIC_MADVENTURE):
            mAdventure = MiniAdventure(name, description, realm, Status.PROGRESSING)
        elif (madventure_type == MAdventureChoice.RELIC_HUNT):
            MAdventureChoice.print_relic_hunt_mode_choices()
            mode_choice = Choice.getIntInput()

            mode = "competitive"
            if (mode_choice == MAdventureChoice.COOP):
                mode = "coop"

            mAdventure = RelicHuntAdventure(name, description, realm, target_relics=2, mode=mode)
        elif (madventure_type == MAdventureChoice.ROYAL_ESCORT):
            mAdventure = EscortAdventure(name, description, realm)
        else:
            print("> Invalid mini-adventure type!\n")
            return

        user.createMAdventure(name, mAdventure)
        mAdventures[name] = mAdventure

        print("> Mini adventure added! Change more details about it in the menu!\n")
    
    @staticmethod
    def remove_madventure(mAdventures: dict, user: User) -> None:
        print("> What is the name of the mini-adventure you want to remove?")
        name = Choice.getStringInput()

        if (name in user.getMAdventures()):
            user.removeMAdventure(name)
            mAdventures.pop(name)
            print("> Mini-adventure removed!\n")
        else:
            print("> That mini-adventure does not exist!\n")

    @staticmethod
    def play_madventure(choiceUI, user: User) -> None:
        MAdventureChoice.print_mini_adventures(choiceUI)

        print("> Type the name of the mini-adventure you want to join:")
        name = Choice.getStringInput()

        if (not MAdventureChoice.name_in_madventures(name, user.getMAdventures())):
            print("> That mini-adventure does not exist!\n")
            return

        adventure = user.getMAdventures()[name]

        if (isinstance(adventure, RelicHuntAdventure) or isinstance(adventure, EscortAdventure)):
            adventure.run()
        else:
            print("> That mini-adventure is not playable yet.\n")
