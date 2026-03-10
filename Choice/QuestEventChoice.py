from Choice.Choice import Choice
from WorldClockTime import WorldClockTime
from QuestEvent import QuestEvent
import uuid

class QuestEventChoice(Choice):
    ADD_QUEST_EVENT = 1
    REMOVE_QUEST_EVENT = 2
    UPDATE_QUEST_EVENT = 3
    RETURN = 4

    @staticmethod
    def printQuestEventChoices() -> None:
        print("> What would you like to do with your quest events? Type the number:")
        print("* (1) Add a new quest event")
        print("* (2) Remove an existing quest event")
        print("* (3) Update an existing quest event")
        print("* (4) Return")

    @staticmethod
    def getQuestEventChoice(campaign) -> None:
        QuestEventChoice.printQuestEventChoices()
        choice = Choice.getStringInput()

        try:
            while (int(choice) != QuestEventChoice.RETURN):
                match (int(choice)):
                    case QuestEventChoice.ADD_QUEST_EVENT:
                        QuestEventChoice.createQuestEvent(campaign)
                    case QuestEventChoice.REMOVE_QUEST_EVENT:
                        QuestEventChoice.removeQuestEvent(campaign)
                    case QuestEventChoice.UPDATE_QUEST_EVENT:
                        QuestEventChoice.updateQuestEvent(campaign)
                    case _:
                        print("> Invalid input! Try again!\n")

                QuestEventChoice.printQuestEventChoices()
                choice = Choice.getStringInput()
        except ValueError:
            print("> Your input is not a number!\n")

    @staticmethod
    def createQuestEvent(campaign) -> None:
        print("> Please enter your quest event title: ")
        title = Choice.getStringInput()

        if (title in campaign.getQuestEvents()):
            print("> That quest event already exists!" + "\n")
            return

        print("> For your start time, please enter (in integers)")

        days = 0
        hours = 0
        minutes = 0

        try:
            print("Days: ")
            days = Choice.getIntInput()

            print("Hours: ")
            hours = Choice.getIntInput()

            print("Minutes: ")
            minutes = Choice.getIntInput()
        except ValueError:
            print("> Your input is not an integer!\n")
            return

        startTime = WorldClockTime(days, hours, minutes)

        questEvent = QuestEvent(uuid.uuid4(), title, startTime)
        campaign.addQuestEvent(title, questEvent)

        print("> New Campaign created!" + "\n")

    @staticmethod
    def removeQuestEvent(campaign) -> None:
        print("> What is the title of the quest event you want to remove?")
        title = Choice.getStringInput()

        if (title in campaign.getQuestEvents()):
            campaign.removeQuestEvent(title)
            print("> Quest event removed!\n")
        else:
            print("> That quest event does not exist!\n")

    @staticmethod
    def updateQuestEvent(campaign) -> None:
        print("> What is the title of the quest event you want to update?")
        questEventTitle = Choice.getStringInput()

        if (questEventTitle in campaign.getQuestEvents()):
            print("> Please enter your new quest event title: ")
            newTitle = Choice.getStringInput()

            print("> For your start time, please enter (in integers)")

            newStartDays = 0
            newStartHours = 0
            newStartMinutes = 0

            try:
                print("Days: ")
                newStartDays = Choice.getIntInput()

                print("Hours: ")
                newStartHours = Choice.getIntInput()

                print("Minutes: ")
                newStartMinutes = Choice.getIntInput()
            except ValueError:
                print("> Your input is not an integer!\n")
                return

            questEvent = campaign.getQuestEvents()[questEventTitle]

            print("> Would you like to update the end time? (Y/N): ")
            choice = Choice.getStringInput()

            if (choice.lower() == "y"):
                print("> For your end time, please enter (in integers)")
                newEndDays = 0
                newEndHours = 0
                newEndMinutes = 0

                try:
                    print("Days: ")
                    newEndDays = Choice.getIntInput()

                    print("Hours: ")
                    newEndHours = Choice.getIntInput()

                    print("Minutes: ")
                    newEndMinutes = Choice.getIntInput()

                    newEndTime = WorldClockTime(newEndDays, newEndHours, newEndMinutes)
                    questEvent.updateEndTime(newEndTime)
                except ValueError:
                    print("> Your input is not an integer!\n")
                    return
            elif (choice.lower() != "n"):
                print("> Your input is not valid!\n")
                return

            newStartTime = WorldClockTime(newStartDays, newStartHours, newStartMinutes)
            questEvent.rename(newTitle)
            questEvent.updateStartTime(newStartTime)

            print("> Quest event updated!\n")
        else:
            print("> That quest event does not exist!\n")
