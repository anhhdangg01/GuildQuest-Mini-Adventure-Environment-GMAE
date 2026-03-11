from choices.choice import Choice
from enums.character_class import CharacterClass
from models.character import Character
from choices.item_choice import ItemChoice
from models.inventory import Inventory
from models.user import User
from typing import Callable
import uuid

class CharacterChoice(Choice):
    ADD_CHARACTER = 1
    REMOVE_CHARACTER = 2
    UPDATE_CHARACTER = 3
    ADD_ITEM = 4
    REMOVE_ITEM = 5
    UPDATE_ITEM = 6
    RETURN = 7

    WARRIOR_CHOICE = 1
    THIEF_CHOICE = 2
    MAGE_CHOICE = 3
    ARCHER_CHOICE = 4
    PRIEST_CHOICE = 5

    InventoryOperation = Callable[["Inventory"], None]

    @staticmethod
    def performInventoryOperation(user: User, operation: InventoryOperation) -> None:
        print("> Type an existing character name:")
        characterName = Choice.getStringInput()

        if (characterName in user.getCharacters()):
            inventory = user.getCharacters().get(characterName).getInventory()
            operation(inventory)
        else:
            print("> That character does not exist!\n")

    @staticmethod
    def printCharacterChoices() -> None:
        print("> What would you like to do with your characters? Type the number:")
        print("* (1) Add a new character")
        print("* (2) Remove an existing character")
        print("* (3) Update an existing character")
        print("* (4) Add an item to an existing character inventory")
        print("* (5) Remove an item from an existing character inventory")
        print("* (6) Update an item from an existing character inventory")
        print("* (7) Return")

    @staticmethod
    def printCharacterClassChoices() -> None:
        print("> Which class do you want your character to be? Type the number of one of the following:")
        print("* (1) Warrior")
        print("* (2) Thief")
        print("* (3) Mage")
        print("* (4) Archer")
        print("* (5) Priest")

    @staticmethod
    def getCharacterClass() -> CharacterClass:
        charClassChoiceNumber = Choice.getIntInput()
        charClass = CharacterClass.PRIEST

        match (charClassChoiceNumber):
            case CharacterClass.WARRIOR.value:
                charClass = CharacterClass.WARRIOR
            case CharacterClass.THIEF.value:
                charClass = CharacterClass.THIEF
            case CharacterClass.MAGE.value:
                charClass = CharacterClass.MAGE
            case CharacterClass.ARCHER.value:
                charClass = CharacterClass.ARCHER
            case CharacterClass.PRIEST.value:
                pass
            case _:
                raise ValueError()

        return charClass

    @staticmethod
    def getCharacterChoice(user: User) -> None:
        CharacterChoice.printCharacterChoices()
        choice = Choice.getStringInput()

        try:
            while (int(choice) != CharacterChoice.RETURN):
                match (int(choice)):
                    case CharacterChoice.ADD_CHARACTER:
                        CharacterChoice.addCharacter(user)
                    case CharacterChoice.REMOVE_CHARACTER:
                        CharacterChoice.removeCharacter(user)
                    case CharacterChoice.UPDATE_CHARACTER:
                        CharacterChoice.updateCharacter(user)
                    case CharacterChoice.ADD_ITEM:
                        CharacterChoice.performInventoryOperation(user, ItemChoice.addItem)
                    case CharacterChoice.REMOVE_ITEM:
                        CharacterChoice.performInventoryOperation(user, ItemChoice.removeItem)
                    case CharacterChoice.UPDATE_ITEM:
                        CharacterChoice.performInventoryOperation(user, ItemChoice.updateItem)
                    case _:
                        print("> Invalid input! Try again!\n")

                CharacterChoice.printCharacterChoices()
                choice = Choice.getStringInput()
        except ValueError:
            print("> Your input is not a number!\n")

    @staticmethod
    def addCharacter(user: User) -> None:
        print("> Please enter your character name: ")
        name = Choice.getStringInput()

        if (name in user.getCharacters()):
            print("> That character already exists!" + "\n")
            return

        CharacterChoice.printCharacterClassChoices()

        try:
            charClass = CharacterChoice.getCharacterClass()

            print("> What level would you like your character to be? Type an integer: ")
            level = Choice.getIntInput()

            newChara = Character(uuid.uuid4(), name, charClass, level)
            user.getCharacters()[name] = newChara

            print("> New character created!" + "\n")
        except ValueError:
            print("> Your input is not a valid integer!\n")

    @staticmethod
    def removeCharacter(user: User) -> None:
        print("> What is the name of the character you want to remove?")
        name = Choice.getStringInput()

        if (name in user.getCharacters()):
            user.getCharacters().pop(name)
            print("> Character removed!\n")
        else:
            print("> That character does not exist!\n")

    @staticmethod
    def updateCharacter(user: User) -> None:
        print("> What is the name of the character you want to update?")
        characterName = Choice.getStringInput()

        try:
            if (characterName in user.getCharacters()):
                print("> Please enter your character's new name: ")
                newName = Choice.getStringInput()

                if (newName in user.getCharacters()):
                    print("> That character name already exists!\n")
                    return

                CharacterChoice.printCharacterClassChoices()
                charClass = CharacterChoice.getCharacterClass()

                print("> What level would you like your character to be? Type an integer: ")
                level = Choice.getIntInput()

                updatedCharacter = user.getCharacters()[characterName]
                updatedCharacter.rename(newName)
                updatedCharacter.changeClass(charClass)
                updatedCharacter.setLevel(level)
                user.getCharacters().pop(characterName)
                user.getCharacters()[newName] = updatedCharacter

                print("> Character updated!" + "\n")
            else:
                print("> That character does not exist!\n")
        except ValueError:
            print("> Your input is not a valid integer!\n")
