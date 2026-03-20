import random
from models.mini_adventure import MiniAdventure
from models.realm import Realm
from models.item import Item
from models.hazard import Hazard
from enums.status import Status
from enums.entity_type import EntityType
from enums.rarity import Rarity
from enums.type import Type

class EscortAdventure(MiniAdventure):
    def __init__(self, realm: Realm, target_coord: tuple = None):
        super().__init__(realm, Status.PROGRESSING)
        
        self.name = "Royal Escort"
        self.description = "Protect the NPC and guide them to the extraction point."
        
        self.width = int(realm.mapIdentity.x)
        self.height = int(realm.mapIdentity.y)
        
        # Define the target goal (default to center or specified)
        self.target_coord = target_coord or (self.width // 2, self.height // 2)
        
        # Initialize players and NPC
        self.players = {
            "Player 1": {"position": [0, 0], "inventory": []},
            "Player 2": {"position": [self.width - 1, 0], "inventory": []},
        }
        self.npc = {"name": "VIP", "position": [0, self.height - 1], "health": 100}
        
        self.turn_order = ["Player 1", "Player 2", "NPC"]
        self.current_turn_index = 0
        
        self.item_positions = {}
        self.hazard_positions = {}
        
        self.add_objective("Escort", f"Get the VIP to {self.target_coord} safely.")
        
        self._validate_realm_size()
        self._setup_entities()

    def _advance_turn(self) -> None:
        self.current_turn_index = (self.current_turn_index + 1) % len(self.turn_order)
        current = self.turn_order[self.current_turn_index]
        
        print(f"Turn order swapped. It is now {current}'s turn.")
        
        if current == "NPC":
            self._move_npc()
            # After NPC moves, cycle back to Player 1
            self._advance_turn()

    def _move_npc(self) -> None:
        """NPC moves automatically toward the target if players are nearby."""
        curr_x, curr_y = self.npc["position"]
        tar_x, tar_y = self.target_coord
        
        # Check if at least one player is within 1 tile (escort mechanic)
        escorted = any(
            abs(p["position"] - curr_x) <= 1 and abs(p["position"] - curr_y) <= 1
            for p in self.players.values()
        )
        
        if not escorted:
            print("The VIP is scared and refuses to move without an escort!")
            return

        # Simple pathfinding toward target
        if curr_x < tar_x: curr_x += 1
        elif curr_x > tar_x: curr_x -= 1
        elif curr_y < tar_y: curr_y += 1
        elif curr_y > tar_y: curr_y -= 1
        
        self.npc["position"] = [curr_x, curr_y]
        print(f"The VIP moves to {self.npc['position']}.")
        
        # Check if NPC hit a hazard
        pos = tuple(self.npc["position"])
        if pos in self.hazard_positions:
            self.npc["health"] -= 20
            print(f"VIP hit a {self.hazard_positions[pos].get_name()}! Health: {self.npc['health']}")
            
        self._check_win_condition()

    def move_player(self, player_name: str, direction: str) -> None:
        if self.status != Status.PROGRESSING or player_name != self.turn_order[self.current_turn_index]:
            return

        x, y = self.players[player_name]["position"]
        moves = {"up": (0, -1), "down": (0, 1), "left": (-1, 0), "right": (1, 0)}
        
        dx, dy = moves.get(direction, (0, 0))
        new_x, new_y = x + dx, y + dy

        if 0 <= new_x < self.width and 0 <= new_y < self.height:
            self.players[player_name]["position"] = [new_x, new_y]
            self._check_tile(player_name)
            self.print_ascii_grid()
            self._advance_turn()

    def _check_tile(self, player_name: str) -> None:
        pos = tuple(self.players[player_name]["position"])
        
        if pos in self.item_positions:
            item = self.item_positions.pop(pos)
            self.players[player_name]["inventory"].append(item.get_name())
            print(f"{player_name} picked up {item.get_name()}!")

        if pos in self.hazard_positions:
            print(f"{player_name} cleared a {self.hazard_positions[pos].get_name()} for the VIP!")
            self.hazard_positions.pop(pos) # Players can "disarm" hazards by stepping on them

    def _check_win_condition(self) -> None:
        if tuple(self.npc["position"]) == self.target_coord:
            self.status = Status.WIN
            print("Mission Success! The VIP has been escorted to safety.")
        elif self.npc["health"] <= 0:
            self.status = Status.FAILED
            print("Mission Failed! The VIP has perished.")

    def print_ascii_grid(self) -> None:
        print(f"\n=== {self.name} === VIP HP: {self.npc['health']} ===")
        npc_pos = tuple(self.npc["position"])
        p1_pos = tuple(self.players["Player 1"]["position"])
        p2_pos = tuple(self.players["Player 2"]["position"])

        print("\n=== Realm Grid ===")
        for y in range(self.height):
            row = []
            for x in range(self.width):
                pos = (x, y)
                if pos == self.target_coord: row.append("[E]") # Exit
                elif pos == npc_pos: row.append("[V]") # VIP
                elif pos == p1_pos: row.append("[1]")
                elif pos == p2_pos: row.append("[2]")
                elif pos in self.hazard_positions: row.append("[X]")
                elif pos in self.item_positions: row.append("[i]")
                else: row.append("[ ]")
            print("".join(row))
        print("Legend: [1]=Player 1  [2]=Player 2 [V]=VIP [E]=Exit [X]=Hazard [i]=Item")

    def _setup_entities(self) -> None:
        # Generate some random hazards and items
        blocked = {tuple(self.npc["position"]), tuple(self.players["Player 1"]["position"]), 
                   tuple(self.players["Player 2"]["position"]), self.target_coord}
        
        item_locs = self._generate_random_positions(2, blocked)
        for loc in item_locs:
            self.item_positions[loc] = Item("medkit", "Medkit", EntityType.ITEM, Rarity.COMMON, Type.PASSIVE)
            blocked.add(loc)
            
        haz_locs = self._generate_random_positions(4, blocked)
        for loc in haz_locs:
            self.hazard_positions[loc] = Hazard("Ambush", EntityType.HAZARD, 10.0)

    def _validate_realm_size(self) -> None:
        if self.width * self.height < 9:
            raise ValueError("Realm too small for an escort mission.")

    def _generate_random_positions(self, count: int, blocked_positions=None) -> list:
        available = [(x, y) for x in range(self.width) for y in range(self.height) 
                     if (x, y) not in (blocked_positions or set())]
        
        return random.sample(available, min(count, len(available)))