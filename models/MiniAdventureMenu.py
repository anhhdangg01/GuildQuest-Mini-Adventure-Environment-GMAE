class MiniAdventureMenu:
    def __init__(self):
        self.adventures = []

    def add_adventure(self, adventure: MiniAdventure) -> None:
        self.adventures.append(adventure)

    def remove_adventure(self, adventure: MiniAdventure) -> bool:
        if adventure in self.adventures:
            self.adventures.remove(adventure)
            return True
        return False
    
    def remove_adventure_by_name(self, name: str) -> bool:
        for adventure in self.adventures:
            if adventure.get_name().lower() == name.lower():
                self.adventures.remove(adventure)
                return True
        return False

    def display_menu(self) -> None:
        print("\n=== GuildQuest Mini-Adventure Menu ===")
        for i, adventure in enumerate(self.adventures, start=1):
            print(f"{i}. {adventure.get_name()} - {adventure.get_description()}")
        print("0. Exit")

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

            print("Invalid choice. Please try again.\n")
