from Choice.ChoiceUI import ChoiceUI

def main() -> None:
    choiceUI = ChoiceUI()

    print("*** Welcome to GuildQuest! ***" + "\n")
    choice = input("> Type in a username, or type [!] to quit: ")

    while (not (choice == "!")):
        user = choiceUI.checkUser(choice)
        choiceUI.getUserChoice(user)

        choice = input("\n> Type in a username, or type [!] to quit: ")


if __name__ == "__main__": main()
