from classes.pirate import Pirate
from classes.item import Medicine, Clothing, Food, PetCompanion


class Planet:
    def __init__(self, name, level_req, takes_fuel, takes_time, description, inventory):
        self.name = name
        self.level_req = level_req
        self.takes_fuel = takes_fuel
        self.takes_time = takes_time
        self.description = description
        self.inventory = inventory

    def display_description(self):
        return f"Welcome to {self.name}! - {self.description}"

    def check_access(self, player_level):
        return player_level >= self.level_req

    def display(self):
        inventory_details = "\n".join(
            f"{i+1}. {item.get_details()['name']} - {item.get_details()['description']} "
            f"({item.get_details()['price']} credits)"
            for i, item in enumerate(self.inventory)
        )
        return f"Items available on {self.name}:\n{inventory_details}"

    def sell(self, player, item_name, quantity):
        if not player.has_item(item_name, quantity):
            return f"You do not have {quantity} {item_name} to sell."

        item_details = player.inventory.get(item_name)
        selling_price = (item_details["price"] // 2) * quantity
        player.remove_from_inventory(item_name, quantity)
        player.credits += selling_price

        return (
            f"Transaction Successful!\n"
            f"You sold {quantity} {item_name} for {selling_price} credits.\n"
            f"New Credit Balance: {player.credits}."
        )

    def buy(self, player, item_index, quantity):
        if not (0 <= item_index < len(self.inventory)):
            return "Invalid item selection."

        item = self.inventory[item_index]
        total_cost = item.price * quantity

        if player.credits < total_cost:
            return f"Insufficient credits. You need {total_cost - player.credits} more credits."

        player.credits -= total_cost

        healing = getattr(item, "healing", 0)
        player.add_to_inventory(item.name, quantity, item.price, healing=healing)
        return (
            f"Transaction Successful!\n"
            f"You purchased {quantity} {item.name} for {total_cost} credits.\n"
            f"Remaining Credits: {player.credits}."
        )


mercantara_inventory = [
    Medicine("Bandages", "Basic wound wraps for small injuries.", 10, 10),
    Food("Protein Bar", "Compact and nutritious.", 10, 5),
    Clothing("Basic Space Suit", "Standard-issue, no frills.", 50, 5),
    PetCompanion("Astro-Kitten", "Cute companion for morale.", 30, "+2 morale boost"),
]

barteron_inventory = [
    Medicine(
        "First Aid Kit", "A compact kit with essential tools for healing.", 50, 20
    ),
    Food("Hydroponic Fruit Pack", "Fresh fruits grown in hydroponic systems.", 50, 15),
    Clothing(
        "Thermal Insulated Cloak", "Keeps you safe in harsh environments.", 200, 15
    ),
    PetCompanion(
        "Quantum Hound",
        "Tracks rare loot during exploration.",
        700,
        "+15% rare loot detection",
    ),
]

voltrade_inventory = [
    Medicine(
        "Regeneration Serum",
        "High-tech serum that regenerates cellular damage.",
        200,
        50,
    ),
    Food("Exotic Alien Cuisine", "Rare dishes from distant worlds.", 150, 30),
    Clothing(
        "Reactive Defense Cloak", "Automatically deflects small attacks.", 800, 35
    ),
    PetCompanion(
        "Void Hawk", "Provides aerial combat support.", 900, "+20 damage in combat"
    ),
]
