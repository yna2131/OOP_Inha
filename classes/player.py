from classes.pirate import Pirate
from classes.ship import Ship, CargoShip, FighterShip


class Player:
    def __init__(self, name):
        self.name = name
        self.level = 1
        self.credits = 100
        self.health = 100
        self.days_passed = 0
        self.inventory = {
            "Rusty Blade": {"damage": 5, "price": 15, "quantity": 1},
            "Basic Laser Pistol": {"damage": 7, "price": 30, "quantity": 1},
            "Basic First Aid Kit": {"healing": 10, "price": 50, "quantity": 1},
        }
        self.ships = {
            "CargoShip": CargoShip(name="Basic Inventory", cargo_space=100),
            "FighterShip": FighterShip(
                name="Basic Fighter",
                weapons={
                    "Laser Gun": {"damage": 15, "fuel_cost": 5},
                    "Plasma Blaster": {"damage": 25, "fuel_cost": 10},
                    "Missile Launcher": {"damage": 40, "fuel_cost": 20},
                },
            ),
        }

    def display_stats(self):
        return {
            "Name": self.name,
            "Level": self.level,
            "Health": self.health,
            "Money": self.credits,
            "Days Passed": self.days_passed,
            "Inventory": self.inventory,
            "Ships": self.ships,
        }

    def add_to_inventory(self, item_name, quantity):
        if item_name in self.inventory:
            self.inventory[item_name]["quantity"] += quantity
        else:
            self.inventory[item_name] = {"quantity": quantity, "price": 0, "damage": 0}

    def remove_from_inventory(self, item_name, quantity):
        if (
            item_name in self.inventory
            and self.inventory[item_name]["quantity"] >= quantity
        ):
            self.inventory[item_name]["quantity"] -= quantity
            if self.inventory[item_name]["quantity"] == 0:
                del self.inventory[item_name]
        else:
            raise ValueError(f"Not enough {item_name} to remove.")

    def has_item(self, item_name, quantity):
        return self.inventory.get(item_name, {}).get("quantity", 0) >= quantity
    
    def recover_health(self, item_name):
        if item_name not in self.inventory:
            return f"You don't have {item_name} in your inventory."

        item = self.inventory[item_name]
        if item["quantity"] <= 0:
            return f"You don't have enough {item_name} to use."

        healing = item.get("healing", 0)
        self.health = min(self.health + healing, 100) 
        self.remove_from_inventory(item_name, 1)

        return f"You used {item_name} and recovered {healing} health. Current health: {self.health}/100."

