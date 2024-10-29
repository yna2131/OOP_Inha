from classes.ship import Ship
from classes.planet import Planet
from classes.inventory import Inventory
from classes.pirate import Pirate
from classes.player import Player

# main.py
# Probably set default information

# Maybe we can receive some values from the user like player's name, and their ship's name
while True:
    player_name = input("Enter your player's name: ").strip()
    if player_name:
        break
    print("Player name can't be empty. Please enter a valid name")

while True:
    ship_name = input("Enter your ship's name: ").strip()
    if ship_name:
        break
    print("Ship name can't be empty. Please enter a valid name")
    
ship = Ship(name=ship_name, cargo_space=100, fuel=500, weapons=10, health=100)

player = Player(name=player_name, money=1000, ship=ship)

print(f"Welcome, {player.name}! You are now captin of the ship {ship.name}. Let's start our journey!")