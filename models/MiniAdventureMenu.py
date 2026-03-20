class MiniAdventureMenu:
    def __init__(self):
        self.adventures = []

    def choose_adventure(self) -> MiniAdventure | None:
        while True:
            self.display_menu()
            choice = input("Choose a mini-adventure: ").strip()

            if choice == "0":
                return None

            if choice.isdigit():
                index = int(choice) - 1
                if 0 <= index < len(self.adventures):
                    return self.adventures[index]

            print("> Invalid choice. Please try again.\n")
