import time
import random
import os
from classes.ship import Ship
from classes.planet import Planet
from classes.inventory import Inventory
from classes.pirate import Pirate
from classes.player import Player
from tutorial import tutorial
from game import run

# main.py
# Probably set default information

# Maybe we can receive some values from the user like player's name, and their ship's name
def game_start():
    os.system('cls')
    print("Hi stranger, welcome to Space Galaxy\n")
    time.sleep(0.5)
    print("""
        ⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣀⡠⠄⠀⠀⠀⠀⠀⠀⠀⠐⠂⠤⢄⣀⣀⠀⠀⠀⠀⠀⠀⠀⠠⠤⢄⣀⠀⠀⠀⠀⠀
    ⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣀⠤⠒⠉⠁⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠈⠑⢦⡀⠀⠀
    ⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢀⡤⠊⠁⠀⠀⠀⠀⣀⣠⣤⣤⣶⣶⣶⣶⣶⣦⣤⣄⣀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠱⡄⠀
    ⠀⠀⠀⠀⠀⠀⠀⠀⢀⠔⠁⠀⠀⠀⣀⣤⣶⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣷⣦⣀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢳⠀
    ⠀⡀⠀⠀⠀⠀⢀⡴⠁⠀⠀⢀⣠⣾⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣟⣿⣿⣿⣿⣿⣷⣤⡀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢸⠀
    ⠀⢰⠀⠀⠀⢠⠎⠀⠀⠀⣠⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣄⠀⠀⠀⠀⠀⠀⠀⠀⡸⠀
    ⠀⠸⡀⠀⣠⠃⠀⠀⢀⣾⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣷⡀⠀⠀⠀⠀⠀⠀⡇⠀
    ⠀⠀⡇⢠⠃⠀⠀⢀⣾⣿⣿⣿⣿⣿⠛⣿⣿⣿⣿⣿⡿⠿⠛⠛⡟⠛⠛⠿⢿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⡄⠀⠀⠀⠀⢠⠃⠀
    ⠀⠀⢃⡏⠀⠀⠀⣼⣿⣿⣿⣿⣿⣿⣿⣿⣿⡿⠛⠁⠀⠀⠀⠀⡇⠀⠀⠀⠀⠈⠙⢿⣿⣿⣿⣿⣾⣿⣿⣿⣿⣷⡀⠀⠀⠀⢸⠀⠀
    ⠀⠀⢸⠀⠀⠀⢰⣿⣿⣿⣿⣿⣿⣿⣿⣿⠏⠀⢠⣇⠀⠀⠀⠀⡇⠀⠀⠀⠀⣰⡆⠀⠙⢿⣿⣿⣿⠿⣿⣿⣿⣿⣇⠀⠀⠀⡇⠀⠀
    ⠀⠀⢸⠀⠀⠀⣸⣿⣿⣿⣿⣿⣿⣿⣿⠃⠀⢠⣿⡯⣆⠀⠀⠀⡇⠉⠀⠀⢰⣿⢹⡄⠀⠘⢿⣿⣧⣵⣼⣿⣿⣿⣿⠀⠀⠀⢃⠀⠀
    ⠀⠀⢸⠀⠀⠀⣿⣿⣟⣿⣿⣿⣿⣿⣏⠀⠀⢸⣿⡇⢸⠀⢀⣤⣷⣄⠀⠀⢸⣿⠀⡇⣀⠀⠸⣿⣿⣿⣿⣿⣿⣿⣿⡄⠀⠀⢸⠀⠀
    ⠀⠀⢸⠀⠀⠀⢻⣿⣿⣿⣿⣿⣿⣿⡏⠀⠀⢸⣿⡇⣸⣶⡟⡿⣿⢢⠙⠲⠾⣿⡀⡇⠋⠐⠀⣿⣿⣿⣿⣿⣿⣿⣿⠁⠀⠀⡌⠀⠀
    ⢸⡄⠸⠀⠀⠀⠸⣿⡿⠋⠉⠙⢿⣿⣇⣠⣤⢼⡋⢃⡴⠋⣰⠁⢿⠈⣆⠀⠀⠀⠉⠳⠤⣀⣸⣿⡿⢛⡏⠉⠻⣿⡇⠀⠀⠀⡇⢀⡇
    ⢸⣿⡄⣇⠀⠀⠀⢻⡁⠀⣀⡤⠞⡫⠛⢑⠖⡭⠂⠉⠀⠀⠃⠀⠀⠀⠈⠀⠀⠀⠀⠀⠀⠀⠀⠈⠓⠾⢄⡀⠀⡿⠁⠀⠀⢰⢁⣾⡇
    ⢸⣿⣿⣼⡄⠀⠀⠀⢣⠻⠿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣾⣾⣶⣶⣶⣶⣿⣷⣶⣶⣶⣶⣶⣶⣶⣶⣶⣶⠿⣳⠁⠀⠀⠀⣎⣾⣿⡇
    ⢸⣿⣿⣿⣷⡀⠀⠀⠀⠳⡀⠀⠀⠈⠉⠉⠙⢿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⡟⠛⢯⡉⠁⠀⢀⡜⠁⠀⠀⠀⣼⣿⣿⣿⡇
    ⢸⣿⣿⣿⣿⣷⣄⠀⠀⠀⠘⢦⡀⠀⠀⠀⠀⠀⠙⢿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⠟⠉⠀⠀⠀⠙⢢⡤⠋⠀⠀⠀⢀⣾⣿⣿⣿⣿⡇
    ⢸⣿⣿⣿⣿⣿⣿⡷⣄⠀⠀⠀⠙⠢⣀⠀⠀⠀⠀⠀⠈⠹⣿⣿⣿⣿⣿⡏⠁⠀⠀⠀⠀⠀⣀⠴⠋⠀⠀⠀⢀⢴⣿⣿⣿⣿⣿⣿⡇
    ⢸⣿⣿⣿⣿⣿⣿⣿⣮⡳⣄⠀⠀⠀⠈⠑⠢⢄⣀⠀⠀⠀⣿⣿⣿⡇⢠⠃⠀⠀⣀⡠⠔⠊⠁⠀⠀⠀⣀⠔⣹⣿⣿⣿⣿⣿⣿⣿⡇
    ⢸⣿⣿⣿⣿⣿⣿⣿⣿⣿⣦⡑⠦⣀⠀⠀⠀⠀⠈⠉⠑⠒⢻⣿⣿⡇⡾⠒⠚⠉⠁⠀⠀⠀⠀⢀⡤⠚⣡⣾⣿⣿⣿⣿⣿⣿⣿⣿⡇
    ⠘⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣦⣌⠑⠦⢄⡀⠀⠀⠀⠀⠈⢿⣿⣿⠃⠀⠀⠀⠀⠀⣀⠤⠚⢁⣴⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⠃
    ⠀⠘⢿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣷⣦⣀⠈⠑⠒⠤⠤⣀⣀⣛⣁⣀⡤⠤⠐⠚⠉⢀⣤⣾⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⠏⠀
    ⠀⠀⠀⠙⠿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣷⣦⣄⡀⠀⠀⠀⠀⠀⠀⠀⢀⣠⣴⣾⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⡿⠟⠁⠀⠀
    ⠀⠀⠀⠀⠀⠀⠉⠉⠉⠉⠉⠉⠉⠉⠉⠉⠉⠉⠉⠉⠉⠙⠲⢤⣀⡠⠔⠚⠉⠉⠉⠉⠉⠉⠉⠉⠉⠉⠉⠉⠉⠉⠉⠁⠀⠀⠀⠀⠀
    """)
    time.sleep(1.5)
    os.system('cls')
    
    while (1):
        print("Select the option you want , and press ENTER")
        print("1. START GAME")
        print("2. HOW TO PLAY")
        print("3. EXIT")
        command = input(">>")
        if command == '1':
            run()
        elif command == '2':
            tutorial()
            os.system('cls')
        elif command == '3':
            print("Thank you for playing")
            time.sleep(1.5)
            break
        else:
            os.system('cls')
            print("Invalid option")
            time.sleep(1.5)
            os.system('cls')
            print()
    
if __name__ == "__main__":
    game_start()