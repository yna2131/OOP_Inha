from pirate import Pirate
from item import Medicine, Clothing, Food, PetCompanion
class Planet:
    def __init__(self, name, level_req, takes_fuel, takes_time, description):
        self.name = name
        self.level_req = level_req
        self.takes_fuel = takes_fuel
        self.takes_time = takes_time
        self.description = description

    def display_description(self):
        return f"Welcome to {self.name}! - {self.description}"
    
    def check_access(self, player_level):
        if player_level >= self.level_req:
            return True
        else:
            return f"Access Denied: Level {self.level_req} required to visit {self.name}."
        
class Trading_Planet(Planet):
    def __init__(self, name, level_req, takes_fuel, takes_time, inventory, description):
        super().__init__(name, level_req, takes_fuel, takes_time, description)
        self.inventory = inventory
        
    def display(self):
        inventory_details = "\n".join(
            f"{i+1}. {item.get_details()['name']} - {item.get_details()['description']} "
            f"({item.get_details()['price']} credits)"
            for i, item in enumerate(self.inventory)
        )
        return f"Items available on {self.name}:\n{inventory_details}"

    def sell(self, player, item_name, quantity):
        for item in self.inventory:
            if item.name == item_name:
                selling_price = (item.price // 2) * quantity
                if player.has_item(item_name, quantity):
                    player.remove_from_inventory(item_name, quantity)
                    player.credits += selling_price
                    return (
                        f"Transaction Successful!\n"
                        f"You sold {quantity} {item_name} for {selling_price} credits.\n"
                        f"New Credit Balance: {player.credits}."
                    )
                return f"You do not have {quantity} {item_name} to sell."
        return f"Item '{item_name}' is not accepted on this planet."
    
    
    def buy(self, player, item_index, quantity):
        if not (0 <= item_index < len(self.inventory)):
            return "Invalid item selection."

        item = self.inventory[item_index]
        total_cost = item.price * quantity

        if player.credits < total_cost:
            return f"Insufficient credits. You need {total_cost - player.credits} more credits."

        player.credits -= total_cost
        player.add_to_inventory(item.name, quantity)
        return (
            f"Transaction Successful!\n"
            f"You purchased {quantity} {item.name} for {total_cost} credits.\n"
            f"Remaining Credits: {player.credits}."
        )

# Planet-Specific Inventories
mercantara_inventory = [
    Medicine("Bandages", "Basic wound wraps for small injuries.", 10, 10),
    Food("Protein Bar", "Compact and nutritious.", 10, 5),
    Clothing("Basic Space Suit", "Standard-issue, no frills.", 50, 5),
    PetCompanion("Astro-Kitten", "Cute companion for morale.", 30, "+2 morale boost"),
]

barteron_inventory = [
    Medicine("First Aid Kit", "A compact kit with essential tools for healing.", 50, 20),
    Food("Hydroponic Fruit Pack", "Fresh fruits grown in hydroponic systems.", 50, 15),
    Clothing("Thermal Insulated Cloak", "Keeps you safe in harsh environments.", 200, 15),
    PetCompanion("Quantum Hound", "Tracks rare loot during exploration.", 700, "+15% rare loot detection"),
]

voltrade_inventory = [
    Medicine("Regeneration Serum", "High-tech serum that regenerates cellular damage.", 200, 50),
    Food("Exotic Alien Cuisine", "Rare dishes from distant worlds.", 150, 30),
    Clothing("Reactive Defense Cloak", "Automatically deflects small attacks.", 800, 35),
    PetCompanion("Void Hawk", "Provides aerial combat support.", 900, "+20 damage in combat"),
]
    
class Fight_Planet(Planet):
    def __init__(self, name, level_req, takes_fuel, takes_time, description, regions):
        super().__init__(name, level_req, takes_fuel, takes_time, description)
        self.regions = regions

    def welcome(self):
        return f"Welcome you have arrived to {self.name}. Please choose region where you would like to go."

    def display_regions(self):
        region_list = "\n".join(f"{i+1}. {region['name']} ({region['difficulty']})" for i, region in enumerate(self.regions))
        return f"Please choose a region:\n{region_list}"

    def get_region(self, index):
        if 0 <= index < len(self.regions):
            return self.regions[index]
        return None
    
    def display_pirates(self, region_index):
        region = self.get_region(region_index)
        if not region:
            return "Invalid region selection."

        pirate_list = "\n".join(
            f"{i+1}. {pirate.name} (Type: {pirate.pirate_type}, Level: {pirate.level})"
            for i, pirate in enumerate(region["pirates"])
        )
        return f"Pirates in {region['name']}:\n{pirate_list}"

    def choose_pirate(self, region_index, pirate_index):
        region = self.get_region(region_index)
        if not region:
            return "Invalid region selection."
        
        pirates = region["pirates"]
        if 0 <= pirate_index < len(pirates):
            return pirates[pirate_index]
        return "Invalid pirate selection."

dark_forest_pirates = [
    Pirate("Sneaky Bandit", "Raider", 1, [("Rusty Blade", 5)], 20),
    Pirate("Forest Raider", "Scout", 2, [("Dagger", 6)], 30),
]

river_pirates = [
    Pirate("River Marauder", "Warrior", 3, [("Trident", 10)], 50),
]

capital_pirates = [
    Pirate("Capital Commander", "Guardian", 8, [("Laser Rifle", 25)], 150),
    Pirate("Big Captain Bloodflame", "Warlord", 10, [("Graviton Cannon", 50)], 200),
]
regions = [
    {"name": "Dark Forest", "difficulty": "Light", "pirates": dark_forest_pirates},
    {"name": "River", "difficulty": "Middle", "pirates": river_pirates},
    {"name": "Capital", "difficulty": "Strong", "pirates": capital_pirates}
]
