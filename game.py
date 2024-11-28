import os
import time
import random
from classes.ship import Ship
from classes.planet import (
    Trading_Planet,
    Fight_Planet,
    mercantara_inventory,
    barteron_inventory,
    regions,
)
from classes.pirate import Pirate
from classes.player import Player


def start():
    print("You have received new missions")
    time.sleep(2)
    print("[Achieve the maximum level of your ships]")
    time.sleep(2)
    print("There is not much choice other than to follow these strange instructions")
    time.sleep(2)
    print("Let's survive.")
    time.sleep(2)


def choice(scene, status=0):
    while True:
        if scene == "start":
            cmd = input(
                """What will I do?
                        1. Rest
                        2. Travel \n"""
            )
            if cmd == "1" or cmd == "2":
                return cmd
            else:
                print("Wrong choice. Press ENTER after inserting an option")
                time.sleep(1.5)
                os.system("cls")
        elif scene == "explore":
            print("There are 3 different planets to travel: ")
            print("1. Mercantara")
            print("2. Barteron")
            print("3. Voltrade")
            cmd = input("Where should I go?\n")
            if cmd in ["1", "2", "3"]:
                return cmd
            else:
                print("Wrong choice. Please choose a valid planet number.")
                time.sleep(1.5)
                os.system("cls")


def encounter_pirate(player, pirate):
    print(f"A pirate appears! {pirate.name} ({pirate.pirate_type}) is ready to fight!")
    time.sleep(1)

    while pirate.health > 0 and player.ship.health > 0:
        print(f"\nYour ship's health: {player.ship.health}")
        print(f"{pirate.name}'s health: {pirate.health}")

        action = input("Do you want to (1) Attack or (2) Flee? ")
        if action == "1":
            player_damage = random.randint(10, 30)
            pirate_response = pirate.take_damage(player_damage)
            print(f"You attacked {pirate.name} and dealt {player_damage} damage!")
            if pirate_response["status"] == "defeated":
                print(f"You defeated {pirate.name}! Congratulations.")
                time.sleep(2)
                os.system("cls")
                return
        elif action == "2":
            flee_success = random.choice([True, False])
            if flee_success:
                print("You successfully fled the pirate!")
                time.sleep(2)
                os.system("cls")
                return
            else:
                print("You failed to flee! The pirate attacks!")
        else:
            print("Invalid action. Try again.")
            continue

        pirate_attack = pirate.attack()
        player.ship.health -= pirate_attack["damage"]
        print(
            f"{pirate.name} attacks with {pirate_attack['weapon']} and deals {pirate_attack['damage']} damage!"
        )

        if player.ship.health <= 0:
            print("Your ship has been destroyed! Game over.")
            time.sleep(2)
            os.system("cls")
            break


def explore_planet(player, planet_num):
    if planet_num == "1":
        planet = Trading_Planet(
            name="Mercantara",
            level_req=1,
            takes_fuel=20,
            takes_time=2,
            description="A bustling trade hub with various goods.",
            inventory=mercantara_inventory,
        )
    elif planet_num == "2":
        planet = Trading_Planet(
            name="Barteron",
            level_req=2,
            takes_fuel=30,
            takes_time=3,
            description="A planet known for its rare resources.",
            inventory=barteron_inventory,
        )
    elif planet_num == "3":
        planet = Fight_Planet(
            name="Voltrade",
            level_req=3,
            takes_fuel=50,
            takes_time=5,
            description="A dangerous place with hostile pirates and fierce challenges.",
            regions=regions,
        )
    else:
        print("Invalid planet number!")
        return

    print(planet.display_description())

    if isinstance(planet, Fight_Planet):
        action_prompt = (
            "Do you want to (1) Buy/Sell, (2) Fight Pirates, or (3) Leave?\n"
        )
    else:
        action_prompt = "Do you want to (1) Buy/Sell or (2) Leave?\n"

    action = input(action_prompt)

    if action == "1" and isinstance(planet, Trading_Planet):
        print(planet.display())
        trade_action = input("Do you want to (1) Buy or (2) Sell?\n")
        if trade_action == "1":
            item_index = int(input("Select an item index to buy: ")) - 1
            quantity = int(input("How many do you want to buy? "))
            print(planet.buy(player, item_index, quantity))
        elif trade_action == "2":
            item_name = input("Enter the name of the item you want to sell: ")
            quantity = int(input("How many do you want to sell? "))
            print(planet.sell(player, item_name, quantity))
        time.sleep(2)
        os.system("cls")

    elif action == "2" and isinstance(planet, Fight_Planet):
        print(planet.display_regions())
        region_choice = int(input("Choose a region number to explore: ")) - 1
        print(planet.display_pirates(region_choice))
        pirate_choice = int(input("Choose a pirate number to fight: ")) - 1
        pirate = planet.choose_pirate(region_choice, pirate_choice)
        if isinstance(pirate, Pirate):
            encounter_pirate(player, pirate)
        else:
            print(pirate)

    elif action == "3" or (action == "2" and not isinstance(planet, Fight_Planet)):
        print(f"You decide to leave {planet.name}.")
        time.sleep(2)
        os.system("cls")
    else:
        print("Invalid choice! Exiting to the main menu.")
        time.sleep(2)
        os.system("cls")


def run():
    os.system("cls")
    start()

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

    print(
        f"Welcome, {player.name}! You are now captain of the ship {ship.name}. Let's start our journey!"
    )
    time.sleep(2)
    os.system("cls")

    while True:
        cmd = choice("start")
        if cmd == "1":
            print("You decide to rest for a while.")
            time.sleep(2)
            os.system("cls")
        elif cmd == "2":
            print("You decide to travel.")
            os.system("cls")
            planet_choice = choice("explore")
            explore_planet(player, planet_choice)

            if random.random() < 0.3:
                random_pirate = Pirate(
                    name="Random Raider",
                    pirate_type="Scout",
                    level=2,
                    weapons=[("Basic Laser Pistol", 15)],
                    health=50,
                )
                encounter_pirate(player, random_pirate)

            continue_game = input("Do you want to continue? (y/n): ")
            if continue_game.lower() != "y":
                print("Thanks for playing!")
                break
            time.sleep(2)
            os.system("cls")


if __name__ == "__main__":
    run()
