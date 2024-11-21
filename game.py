import os
import time
import random
from classes.ship import Ship
from classes.planet import Planet
from classes.inventory import Inventory
from classes.pirate import Pirate
from classes.player import Player

def start():
    print("You have receieved new missions")
    time.sleep(2)
    print("[Achieve the maximum level of your ships]")
    time.sleep(2)
    print("There is no much other choice, then to follow this weird instruction")
    time.sleep(2)
    print("Let's survive.")
    time.sleep(2)
    
def choice(scene, status=0):
    while(True):
        if scene == "start":
            cmd = input(""""What will I do?
                            1. Rest
                            2. Travel \n""")
            if cmd == '1' or cmd == '2':
                return cmd
            else:
                print("Wrong choice Press ENTER after inserting an option")
                time.sleep(1.5)
                os.system("cls")
        elif scene == "explore":
            cmd = input("""Where should I go?
                            1. Planet 1
                            2. Planet 2
                            3. Planet 3
                            4. Planet 4
                            5. Planet 5 \n""")

    
def run():        
    os.system('cls')
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
    time.sleep(2)
    os.system('cls')