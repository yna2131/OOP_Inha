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