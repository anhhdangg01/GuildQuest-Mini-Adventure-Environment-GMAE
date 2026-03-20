from choices.choice import Choice
from models.user import User
from models.mini_adventure import MiniAdventure
from models.entity import Entity
from models.rule import Rule
from models.objective import Objective
from enums.entity_type import EntityType
from enums.status import Status

class MAdventureChoice(Choice):
    ADD_MADVENTURE = 1
    REMOVE_MADVENTURE = 2
    CHANGE_REALM = 3
    ADD_ENTITY = 4
    ADD_RULE = 5
    ADD_OBJECTIVE = 6
    CHANGE_STATUS = 7
    JOIN_MADVENTURE = 8
    QUEST_EVENTS = 9
    RETURN = 10

    NPC = 1
    ITEM = 2
    HAZARD = 3

    WIN = 1
    LOSE = 2
    PROGRESSING = 3
    COMPLETE = 4

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
        print("* (3) Change realm of mini-adventure")
        print("* (4) Add entity to mini-adventure")
        print("* (5) Add rule to mini-adventure")
        print("* (6) Add objective mini-adventure")
        print("* (7) Change status of mini-adventure")
        print("* (8) Join mini-adventure (WIP)")
        print("* (9) Quest events")
        print("* (10) Return")

    @staticmethod
    def print_entity_type_choices() -> None:
        print("> What would you like to do with mini-adventures? Type an integer:")
        print("* (1) NPC")
        print("* (2) Item")
        print("* (3) Hazard")

    @staticmethod
    def print_status_choices() -> None:
        print("> What do you want to set the mini-adventure's status as? Choose an integer:")
        print("* (1) Win")
        print("* (2) Lose")
        print("* (3) Progressing")
        print("* (4) Complete")

    @staticmethod
    def get_madventure_choice(choiceUI, user: User) -> None:
        MAdventureChoice.print_madventure_choices()
        choice = Choice.getStringInput()
        
        try:
            while(int(choice) != MAdventureChoice.RETURN):
                match (int(choice)):
                    case MAdventureChoice.ADD_MADVENTURE:
                        MAdventureChoice.add_madventure(choiceUI.userData.realms, user)
                    case MAdventureChoice.REMOVE_MADVENTURE:
                        MAdventureChoice.remove_madventure(user)
                    case MAdventureChoice.CHANGE_REALM:
                        MAdventureChoice.change_realm(choiceUI.userData.realms, user)
                    case MAdventureChoice.ADD_ENTITY:
                        MAdventureChoice.add_entity(user)
                    case MAdventureChoice.ADD_RULE:
                        MAdventureChoice.add_rule(user)
                    case MAdventureChoice.ADD_OBJECTIVE:
                        MAdventureChoice.add_objective(user)
                    case MAdventureChoice.CHANGE_STATUS:
                        MAdventureChoice.change_status(user)
                    case MAdventureChoice.JOIN_MADVENTURE:
                        pass
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
    def add_madventure(realms: dict, user: User) -> None:
        print("> Please enter your mini-adventure name:")
        name = Choice.getStringInput()

        if (MAdventureChoice.name_in_madventures(name, user.getMAdventures())):
            print("> That mini-adventure already exists!\n")
            return
        
        print("> Please choose the realm you want your mini-adventure to take place in: ")

        realm_str = Choice.getStringInput()
        if (realm_str not in realms):
            print("> That realm does not exist!\n")
            return
        
        realm = realms[realm_str]

        mAdventure = MiniAdventure(realm, Status.PROGRESSING)
        user.createMAdventure(name, mAdventure)

        print("> Mini adventure added! Change more details about it in the menu!\n")
    
    @staticmethod
    def remove_madventure(user: User) -> None:
        print("> What is the name of the mini-adventure you want to remove?")
        name = Choice.getStringInput()

        if (name in user.getMAdventures()):
            user.removeMAdventure(name)
            print("> Mini-adventure removed!\n")
        else:
            print("> That mini-adventure does not exist!\n")
    
    @staticmethod
    def change_realm(realms: dict, user: User) -> None:
        print("> What is the name of the mini-adventure you want to edit?")
        name = Choice.getStringInput()

        if (not MAdventureChoice.name_in_madventures(name, user.getMAdventures())):
            print("> That mini-adventure does not exist!\n")
            return

        print("> Which realm do you want to select?")
        realm = Choice.getStringInput()

        if (realm not in realms):
            print("> That realm does not exist!\n")
            return
        
        print("> Realm changed!")
        
    @staticmethod
    def add_entity(user: User) -> None:
        print("> What is the name of the mini-adventure you want to edit?")
        mAdventure_name = Choice.getStringInput()

        if (not MAdventureChoice.name_in_madventures(mAdventure_name, user.getMAdventures())):
            print("> That mini-adventure does not exist!\n")
            return

        print("> What name do you want your entity?")
        entity_name = Choice.getStringInput()

        print("> What type do you want your entity to be?")
        type_choice = Choice.getIntInput()
        type = EntityType.NPC
        match (type_choice):
            case MAdventureChoice.NPC:
                pass
            case MAdventureChoice.ITEM:
                type = EntityType.ITEM
            case MAdventureChoice.HAZARD:
                type = EntityType.HAZARD
            case _:
                print("> Invalid input! Try again!\n")
                return
        
        entity = Entity(entity_name, type)
        user.add_entity(mAdventure_name, entity)

        print("> Entity added!\n")
    
    @staticmethod
    def add_rule(user: User) -> None:
        print("> What is the name of the mini-adventure you want to edit?")
        mAdventure_name = Choice.getStringInput()

        if (not MAdventureChoice.name_in_madventures(mAdventure_name, user.getMAdventures())):
            print("> That mini-adventure does not exist!\n")
            return

        print("> What is your rule's name?")
        rule_name = Choice.getStringInput()
        print("> Please state a rule: ")
        rule_desc = Choice.getStringInput()

        rule = Rule(rule_name, rule_desc)
        user.add_rule(mAdventure_name, rule)

        print("> Rule added!\n")

    @staticmethod
    def add_objective(user: User) -> None:
        print("> What is the name of the mini-adventure you want to edit?")
        mAdventure_name = Choice.getStringInput()

        if (not MAdventureChoice.name_in_madventures(mAdventure_name, user.getMAdventures())):
            print("> That mini-adventure does not exist!\n")
            return

        print("> What is your objective's name?")
        objective_name = Choice.getStringInput()
        print("> Please state an objective: ")
        objective_desc = Choice.getStringInput()

        objective = Rule(objective_name, objective_desc)
        user.add_rule(mAdventure_name, objective)

        print("> Objective added!\n")

    @staticmethod
    def change_status(user: User) -> None:
        print("> What is the name of the mini-adventure you want to edit?")
        name = Choice.getStringInput()

        if (not MAdventureChoice.name_in_madventures(name, user.getMAdventures())):
            print("> That mini-adventure does not exist!\n")
            return

        MAdventureChoice.print_status_choices()
        status_choice = Choice.getIntInput()

        match (status_choice):
            case MAdventureChoice.WIN:
                user.change_status(name, Status.WIN)
            case MAdventureChoice.LOSE:
                user.change_status(name, Status.LOSE)
            case MAdventureChoice.PROGRESSING:
                user.change_status(name, Status.PROGRESSING)
            case MAdventureChoice.COMPLETE:
                user.change_status(name, Status.COMPLETE)
            case _:
                print("> Invalid input! Try again!\n")
                return

        print("> Mini-adventure status updated!\n")