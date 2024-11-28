import random

class Ship:
    def __init__(self, name, cargo_space, weapons, fuel=30, level=1, upgrade_price=500):
        self.name = name
        self.cargo_space = cargo_space
        self.fuel = fuel
        self.weapons = weapons
        self.level = level
        self.upgrade_price = upgrade_price
    
    def upgrade(self, credits):
        pass
    
    def recover(self):
        pass

class CargoShip(Ship):
    def __init__(self, cargo_space, level=1, upgrade_price=500):
        super().__init__(cargo_space, level, upgrade_price)
        self.cargo_space = cargo_space
        self.current_capacity = 0
        self.items = {}
        
    def add(self, item, quantity):
        if self.current_capacity + quantity > self.cargo_space:
            return f"Not enough space for {quantity} {item}(s)."
        if item in self.items:
            self.items[item] += quantity
        else:
            self.items[item] = quantity
        self.current_capacity += quantity
        return f"Added {quantity} {item}(s) to the cargo."
    
    def remove(self, item, quantity):
        if item not in self.items:
            return f"{item} is not in the cargo."
        if self.items[item] < quantity:
            return f"Not enough {item} to remove. Available: {self.items[item]}"
        self.items[item] -= quantity
        self.current_capacity -= quantity
        if self.items[item] == 0:
            del self.items[item]
        return f"Removed {quantity} {item}(s). Current capacity: {self.current_capacity}/{self.cargo_space}"

    def display(self):
        if not self.items:
            return "The cargo is empty."
        else:
            display_text = "Cargo contents:\n"
            for item, quantity in self.items.items():
                display_text += f" - {item}: {quantity}\n"
            display_text += f"Total capacity used: {self.current_capacity}/{self.cargo_space}"
            return display_text

    def upgrade(self, credits):
        if credits >= self.upgrade_price:
            self.level += 1
            self.cargo_space *= 2
            self.upgrade_price *= 2
            return (f"Cargo Ship has been upgraded to level {self.level}!\n"
                    f"Current cargo capacity is {self.cargo_space}.\n"
                    f"Upgrade price is now {self.upgrade_price} credits.")
        else:
            return f"Not enough credits for upgrade. Current upgrade price: {self.upgrade_price} credits."

class FighterShip(Ship):
    def __init__(self, name, weapons, fuel=30, health=100, max_health=100, level=1, upgrade_price=500, dodge_chance=0.2):
        super().__init__(name, fuel, weapons, level, upgrade_price)
        self.health = health
        self.max_health = max_health
        self.dodge_chance = dodge_chance
        # I assumed that weapons is a nested dictionary, and it looks like: weapons = {"Lasers": {"damage": 20, "fuel_cost": 15},
        # "Plasma Cannon": {"damage": 30, "fuel_cost": 20},
        # "Railgun": {"damage": 40, "fuel_cost": 25},
        # }

    def attack(self, enemy, weapon_choice):
        if self.fuel <= 0:
            return f"{self.name} has no fuel to attack!"

        weapon_stats = self.weapons[weapon_choice]
        if self.fuel < weapon_stats['fuel_cost']:
            return (f"Not enough fuel to use {weapon_choice}. "
                    f"Required: {weapon_stats['fuel_cost']}, Available: {self.fuel}")

        # Apply damage and reduce fuel
        damage = weapon_stats['damage']
        self.fuel -= weapon_stats['fuel_cost']
        enemy.take_damage(damage)
        return (f"{self.name} attacks {enemy} with {weapon_choice}, causing {damage} damage.\n"
                f"Fuel remaining: {self.fuel}")

    def take_damage(self, damage):
        if self.dodge():
            return "You successfully dodged the attack!"
        else:
            self.health -= damage
        if self.health <= 0:
            self.health = 0
            return f"{self.name} has been destroyed!"
        return (f"{self.name} received {damage} damage!\n"
                f"Current health: {self.health}.")

    def dodge(self):
        return random.random() < self.dodge_chance

    def upgrade(self, credits):
        # It is not finished version of upgrade multipliers, and they are changeable
        if credits >= self.upgrade_price:
            self.level += 1
            self.fuel *= 2
            self.max_health += 100
            self.dodge_chance += 0.05
            self.upgrade_price *= 2
            return (f"{self.name} has been upgraded to level {self.level}!\n"
                    f"Current weapons: {self.weapons}, Health: {self.health}, Fuel: {self.fuel}l.\n"
                    f"Upgrade price is now {self.upgrade_price} credits.")
        else:
            return f"Not enough credits for upgrade. Current upgrade price: {self.upgrade_price} credits."

    def recover(self):
        self.health = self.max_health
        return f"{self.name}'s health is fully recovered!"

class PirateShip(Ship):
    def __init__(self, name, fuel, level, weapons, health):
        super().__init__(name, fuel, level, weapons)
        self.health = health

    def attack(self, player, weapon_random):
        if self.fuel <= 0:
            return f"{self.name} has no fuel to attack!"
        # Pirate ships choose weapons randomly
        weapon_random = random.choice(list(self.weapons.keys()))
        weapon_stats = self.weapons[weapon_random]
        if self.fuel < weapon_stats['fuel_cost']:
            return f"{self.name} tried to use {weapon_random}, but didn't have enough fuel!"

        # Apply damage and reduce fuel
        damage = weapon_stats['damage']
        self.fuel -= weapon_stats['fuel_cost']
        player.take_damage(damage)
        return f"{self.name} attacks {player} with {weapon_random}, causing {damage} damage."

    def take_damage(self, damage):
        self.health -= damage
        if self.health <= 0:
            self.health = 0
            return f"{self.name} has been destroyed!"
        return (f"{self.name} received {damage} damage!\n"
                f"{self.name} health: {self.health}.")