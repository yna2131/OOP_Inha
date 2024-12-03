import random

class Ship:
    def __init__(self, name):
        self.name = name

class CargoShip(Ship):
    def __init__(self, name, cargo_space):
        super().__init__(name)
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

class FighterShip(Ship):
    def __init__(self, name, weapons, max_fuel=100, max_health=100, dodge_chance=0.2):
        super().__init__(name)
        self.fuel = max_fuel
        self.max_fuel = max_fuel
        self.health = max_health
        self.max_health = max_health
        self.weapons = weapons
        self.dodge_chance = dodge_chance

    def attack(self, enemy, weapon_choice):
        weapon = self.weapons.get(weapon_choice)
        if not weapon:
            return f"{weapon_choice} is not a valid weapon."
        if self.fuel < weapon["fuel_cost"]:
            return f"Not enough fuel to use {weapon_choice}."
        
        self.fuel -= weapon["fuel_cost"]
        damage = weapon["damage"]
        
        result = enemy.take_damage(damage)
        enemy_status = f"{enemy.name} took {damage} damage! Remaining health: {result['remaining_health']}"
        if result["status"] == "defeated":
                enemy_status += f" {enemy.name} has been defeated!"
                
        return f"Attacked {enemy.name} with {weapon_choice}, causing {damage} damage!"

    def take_damage(self, damage):
        if random.random() < self.dodge_chance:
            return "Dodged the attack!"
        self.health = max(0, self.health - damage)
        if self.health == 0:
            return f"{self.name} has been destroyed!"
        return f"{self.name} took {damage} damage. Health: {self.health}/{self.max_health}."

    def recover(self):
        self.fuel = self.max_fuel
        return f"{self.name} is fully restored!"