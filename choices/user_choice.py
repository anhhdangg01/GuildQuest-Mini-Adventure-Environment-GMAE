from choices.choice import Choice
from user import User
import uuid

class UserChoice(Choice):
    CAMPAIGNS = 1
    CHARACTERS = 2
    REALMS = 3
    LOGOUT = 4

    @staticmethod
    def printUserChoices() -> None:
        print("> What would you like to do? Type the number of one of the following:")
        print("* (1) Mini Adventures (WIP)")
        print("* (2) Characters")
        print("* (3) Realms")
        print("* (4) Logout")

    @staticmethod
    def checkUser(username: str, users: dict) -> User:
        # checks if user exists
        try:
            user = users[username]
            print("> Username found! Welcome back, " + username + "\n")
            return user
        except KeyError:
            newUser = User(uuid.uuid4(), username)
            users[username] = newUser
            print("> User created! Welcome, " + username + "\n")
            return newUser
        
    @staticmethod
    def getUserChoice(choiceUI, user: User) -> None:
        UserChoice.printUserChoices()
        choice = Choice.getStringInput()

        try:
            while (int(choice) != UserChoice.LOGOUT):
                match (int(choice)):
                    # case UserChoice.CAMPAIGNS.value:
                    #     choiceUI.getCampaignChoice(user)
                    case UserChoice.CHARACTERS:
                        choiceUI.getCharacterChoice(user)
                    case UserChoice.REALMS:
                        choiceUI.getRealmChoice()
                    case _:
                        print("> Invalid input! Try again!" + "\n")

                UserChoice.printUserChoices()
                choice = Choice.getStringInput()
        except ValueError:
            print("> Your input is not a number!" + "\n")

        print("*** We look forward to seeing you again! ***")
