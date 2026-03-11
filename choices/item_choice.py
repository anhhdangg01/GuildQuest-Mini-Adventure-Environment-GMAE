from choices.choice import Choice
from models.item import Item
from models.inventory import Inventory
from enums.rarity import Rarity
from enums.type import Type
import uuid

class ItemChoice(Choice):
    COMMON = 1
    RARE = 2
    LEGENDARY = 3

    CONSUMABLE = 1
    PASSIVE = 2

    @staticmethod
    def printItemRarities() -> None:
        print("> What do you want your item rarity to be? Type a number: ")
        print("* (1) Common")
        print("* (2) Rare")
        print("* (3) Legendary")

    @staticmethod
    def printItemTypes() -> None:
        print("> What item type do you want? Type a number: ")
        print("* (1) Consumable")
        print("* (2) Passive")

    @staticmethod
    def addItem(inventory: Inventory) -> None:
        print("> Please enter your item name: ")
        name = Choice.getStringInput()

        if (name in inventory.getItems()):
            print("> That item already exists!")
            return
        
        ItemChoice.printItemRarities()

        try:
            rarityChoice = Choice.getIntInput()
            rarity = Rarity.COMMON

            match (rarityChoice):
                case ItemChoice.COMMON:
                    pass
                case ItemChoice.RARE:
                    rarity = Rarity.RARE
                case ItemChoice.LEGENDARY:
                    rarity = Rarity.LEGENDARY
                case _:
                    print("> Invalid input! Try again!" + "\n")
                    return

            ItemChoice.printItemTypes()

            typeChoice = Choice.getIntInput()
            type = Type.CONSUMABLE

            match (typeChoice):
                case ItemChoice.CONSUMABLE:
                    pass
                case ItemChoice.PASSIVE:
                    type = Type.PASSIVE
                case _:
                    print("> Invalid input! Try again!" + "\n")
                    return

            item = Item(uuid.uuid4(), name, rarity, type)
            inventory.addItem(name, item)

            print("> Item added!")
        except ValueError:
            print("> Your input is not an integer!\n")

    def removeItem(inventory: Inventory) -> None:
        print("> What is the name of the item you want to remove?")
        name = Choice.getStringInput()

        if (name in inventory.getItems()):
            inventory.getItems().pop(name)
            print("> Item removed!\n")
        else:
            print("> That item does not exist!\n")

    def updateItem(inventory: Inventory) -> None:
        print("> Please enter the item you want to update: ")
        name = Choice.getStringInput()

        if (not (name in inventory.getItems())):
            print("> That item does not exist!\n")
            return

        print("> Enter a new name for the item: ")
        newName = Choice.getStringInput()

        if (newName in inventory.getItems()):
            print("> That item already exists!")
            return

        ItemChoice.printItemRarities()

        try:
            rarityChoice = Choice.getIntInput()
            rarity = Rarity.COMMON

            match (rarityChoice):
                case ItemChoice.COMMON:
                    pass
                case ItemChoice.RARE:
                    rarity = Rarity.RARE
                case ItemChoice.LEGENDARY:
                    rarity = Rarity.LEGENDARY
                case _:
                    print("> Invalid input! Try again!" + "\n")
                    return

            ItemChoice.printItemTypes()
            typeChoice = Choice.getIntInput()
            type = Type.CONSUMABLE

            match (typeChoice):
                case ItemChoice.CONSUMABLE:
                    pass
                case ItemChoice.PASSIVE:
                    type = Type.PASSIVE
                case _:
                    print("> Invalid input! Try again!" + "\n")
                    return

            updatedItem = inventory.getItems()[name]
            updatedItem.rename(newName)
            updatedItem.setRarity(rarity)
            updatedItem.setType(type)
            inventory.getItems().pop(name)
            inventory.getItems()[newName] = updatedItem

            print("> Item updated!\n")
        except ValueError:
                print("> Your input is not an integer!\n")
        