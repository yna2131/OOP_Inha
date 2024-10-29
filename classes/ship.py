class Ship:
    def __init__(self, name, cargo_space, fuel, weapons, health):
        self.name = name
        self.cargo_space = cargo_space
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
    pass

class FighterShip(Ship):
    pass
