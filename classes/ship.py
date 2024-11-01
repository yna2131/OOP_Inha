class Ship:
    def __init__(self, name, cargo_space, fuel, weapons, health):
        self.name = name
        self.cargo_space = cargo_space # this would be better to define like self.inventory = Inventory(cargo_space) maybe
        self.fuel = fuel
        self.weapons = weapons
        self.health = health

    def trade(self):
        pass
    
    def combat(self):
        pass
    
    def upgrade(self):
        pass
    
class CargoShip(Ship):
    def __init__(self, max_capacity):
        self.max_capacity = max_capacity
        self.current_capacity = 0
        self.items = {}
        
    def add(self):
        pass
    
    def remove(self):
        pass
    
    def display(slef):
        pass
    
# The basic logics realted to managing items; we can add, remove, and display items

class FighterShip(Ship):
    pass

# Maybe we could add a dictionary to track the items stored in the ship; like key being the item name, and the value being the quantity of the item