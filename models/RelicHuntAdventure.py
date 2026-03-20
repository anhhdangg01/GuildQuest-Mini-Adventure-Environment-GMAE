import random

from models.mini_adventure import MiniAdventure
from models.realm import Realm
from models.item import Item
from models.hazard import Hazard
from enums.status import Status
from enums.entity_type import EntityType
from enums.rarity import Rarity
from enums.type import Type


class RelicHuntAdventure(MiniAdventure):
    def __init__(
        self,
        name: str,
        description: str,
        realm: Realm,
        target_relics: int = 2,
        mode: str = "competitive"
    ):
        super().__init__(name, description, realm, Status.PROGRESSING)

        self.mode = mode.lower()
        self.name = "Relic Hunt"
        self.description = (
            "Two players explore the realm, collect relics, and avoid hazards."
        )

        self.target_relics = target_relics
        self.width = int(realm.mapIdentity.x)
        self.height = int(realm.mapIdentity.y)

        self.players = {
            "Player 1": {"position": [0, 0], "relics": 0},
            "Player 2": {"position": [self.width - 1, self.height - 1], "relics": 0},
        }

        self.turn_order = ["Player 1", "Player 2"]
        self.current_turn_index = 0

        self.team_relics = 0
        self.relic_positions = {}
        self.hazard_positions = {}

        if self.mode == "coop":
            self.add_objective(
                "Team Relic Goal",
                f"Work together to collect {self.target_relics} relics."
            )
        else:
            self.add_objective(
                "Collect Relics",
                f"Be the first player to collect {self.target_relics} relics."
            )

        self._validate_realm_size()
        self._setup_entities()

    def get_name(self) -> str:
        if self.mode == "coop":
            return f"{self.name} (Co-Op)"
        return f"{self.name} (Competitive)"

    def get_description(self) -> str:
        if self.mode == "coop":
            return (
                "Two players work together to collect relics scattered across the realm "
                "while avoiding hazards."
            )
        return (
            "Two players compete to collect relics scattered across the realm "
            "while avoiding hazards."
        )

    def get_current_player(self) -> str:
        return self.turn_order[self.current_turn_index]

    def _advance_turn(self) -> None:
        self.current_turn_index = (self.current_turn_index + 1) % len(self.turn_order)
        print(f"Turn order swapped. It is now {self.get_current_player()}'s turn.")

    def _validate_realm_size(self) -> None:
        total_tiles = self.width * self.height
        required_tiles = 7

        if total_tiles < required_tiles:
            raise ValueError(
                "This realm is too small for Relic Hunt. "
                "Players must choose a bigger realm."
            )

    def _generate_random_positions(self, count: int, blocked_positions=None) -> list:
        if blocked_positions is None:
            blocked_positions = set()

        available_positions = []

        for x in range(self.width):
            for y in range(self.height):
                if (x, y) not in blocked_positions:
                    available_positions.append((x, y))

        if count > len(available_positions):
            raise ValueError(
                "Not enough open tiles in this realm. "
                "Players must choose a bigger realm."
            )

        return random.sample(available_positions, count)

    def _setup_entities(self) -> None:
        relic_1 = Item(
            "relic_1",
            "King's Crown",
            EntityType.ITEM,
            Rarity.RARE,
            Type.PASSIVE
        )
        relic_2 = Item(
            "relic_2",
            "Sacred Chalice",
            EntityType.ITEM,
            Rarity.LEGENDARY,
            Type.PASSIVE
        )

        spike_trap = Hazard("Spike Trap", EntityType.HAZARD, 10.0)
        wall = Hazard("Wall", EntityType.HAZARD, 5.0)
        pit = Hazard("Pit", EntityType.HAZARD, 12.0)

        relics = [relic_1, relic_2]
        hazards = [spike_trap, wall, pit]

        for relic in relics:
            self.add_entity(relic)

        for hazard in hazards:
            self.add_entity(hazard)

        blocked_positions = {
            tuple(self.players["Player 1"]["position"]),
            tuple(self.players["Player 2"]["position"]),
        }

        relic_tiles = self._generate_random_positions(len(relics), blocked_positions)

        for i in range(len(relics)):
            self.relic_positions[relic_tiles[i]] = relics[i]

        blocked_positions.update(relic_tiles)

        hazard_tiles = self._generate_random_positions(len(hazards), blocked_positions)

        for i in range(len(hazards)):
            self.hazard_positions[hazard_tiles[i]] = hazards[i]

    def move_player(self, player_name: str, direction: str) -> None:
        if self.status != Status.PROGRESSING:
            return

        if player_name not in self.players:
            return

        if player_name != self.get_current_player():
            print(f"It is not {player_name}'s turn.")
            return

        x, y = self.players[player_name]["position"]

        if direction == "up" and y > 0:
            y -= 1
        elif direction == "down" and y < self.height - 1:
            y += 1
        elif direction == "left" and x > 0:
            x -= 1
        elif direction == "right" and x < self.width - 1:
            x += 1
        else:
            print("Invalid move direction.")
            return

        self.players[player_name]["position"] = [x, y]
        self._check_tile(player_name)
        self.print_ascii_grid()

        if self.status == Status.PROGRESSING:
            self._advance_turn()

    def _check_tile(self, player_name: str) -> None:
        pos = tuple(self.players[player_name]["position"])

        if pos in self.relic_positions:
            relic = self.relic_positions.pop(pos)
            self.players[player_name]["relics"] += 1
            self.team_relics += 1
            print(f"{player_name} collected {relic.get_name()}!")

            if self.mode == "coop":
                print(f"Team relic total: {self.team_relics}/{self.target_relics}")

        if pos in self.hazard_positions:
            hazard = self.hazard_positions[pos]
            hazard.trigger()
            print(f"{player_name} triggered {hazard.get_name()}!")

        self._check_win_condition()

    def _check_win_condition(self) -> None:
        if self.mode == "coop":
            if self.team_relics >= self.target_relics:
                self.status = Status.WIN
                print("Both players win the Co-Op Relic Hunt!")
                return
        else:
            for current_player_name, data in self.players.items():
                if data["relics"] >= self.target_relics:
                    self.status = Status.WIN
                    print(f"{current_player_name} wins Relic Hunt!")
                    return

        if len(self.relic_positions) == 0:
            self.status = Status.COMPLETE
            print("All relics have been collected. The mini-adventure is complete.")

    def print_ascii_grid(self) -> None:
        print("\n=== Realm Grid ===")

        player_1_pos = tuple(self.players["Player 1"]["position"])
        player_2_pos = tuple(self.players["Player 2"]["position"])

        for y in range(self.height):
            row = []
            for x in range(self.width):
                pos = (x, y)

                if pos == player_1_pos and pos == player_2_pos:
                    row.append("[B]")
                elif pos == player_1_pos:
                    row.append("[1]")
                elif pos == player_2_pos:
                    row.append("[2]")
                elif pos in self.relic_positions:
                    row.append("[R]")
                elif pos in self.hazard_positions:
                    hazard_name = self.hazard_positions[pos].get_name()
                    if hazard_name == "Spike Trap":
                        row.append("[T]")
                    elif hazard_name == "Wall":
                        row.append("[W]")
                    elif hazard_name == "Pit":
                        row.append("[P]")
                    else:
                        row.append("[H]")
                else:
                    row.append("[ ]")
            print("".join(row))

        print(
            "Legend: [1]=Player 1  [2]=Player 2  [R]=Relic  "
            "[T]=Spike Trap  [W]=Wall  [P]=Pit\n"
        )

    def get_player_position(self, player_name: str):
        return self.players[player_name]["position"]

    def get_player_relic_count(self, player_name: str) -> int:
        return self.players[player_name]["relics"]

    def get_state(self) -> dict:
        return {
            "name": self.get_name(),
            "description": self.get_description(),
            "mode": self.mode,
            "realm": self.realm.name,
            "status": self.status.name,
            "current_player": self.get_current_player(),
            "players": self.players,
            "team_relics": self.team_relics,
            "remaining_relic_positions": list(self.relic_positions.keys()),
            "hazard_positions": list(self.hazard_positions.keys()),
            "objective": {
                name: obj.get_description()
                for name, obj in self.objectives.items()
            },
        }

    def reset(self) -> None:
        self.status = Status.PROGRESSING
        self.team_relics = 0
        self.current_turn_index = 0

        self.players["Player 1"] = {"position": [0, 0], "relics": 0}
        self.players["Player 2"] = {
            "position": [self.width - 1, self.height - 1],
            "relics": 0
        }

        self.relic_positions.clear()
        self.hazard_positions.clear()
        self.entities.clear()
        self.objectives.clear()

        if self.mode == "coop":
            self.add_objective(
                "Team Relic Goal",
                f"Work together to collect {self.target_relics} relics."
            )
        else:
            self.add_objective(
                "Collect Relics",
                f"Be the first player to collect {self.target_relics} relics."
            )

        self._validate_realm_size()
        self._setup_entities()
        self.print_ascii_grid()