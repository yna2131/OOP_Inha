import os
import time
import random
from classes.pirate import Pirate
from classes.player import Player
from classes.planet import (
    Planet,
    mercantara_inventory,
    barteron_inventory,
    voltrade_inventory,
)


def clear_screen():
    os.system("cls" if os.name == "nt" else "clear")


def start():
    print("You have received new missions.")
    time.sleep(2)
    print("[Earn 2000 credits as quickly as possible!]")
    time.sleep(2)
    print("There is not much choice other than to follow these strange instructions.")
    time.sleep(2)
    print("Let's survive.")
    time.sleep(2)


def choice(scene, prompt=None, options=None):
    while True:
        print(prompt)
        cmd = input("Tell us your decision: ").strip()
        if cmd in options:
            return cmd
        else:
            print("Invalid choice. Please try again.")
            time.sleep(1.5)
            clear_screen()


def encounter_pirate(player):
    if player.ships["FighterShip"].fuel <= 0:
        print("You are out of fuel and cannot fight pirates!")
        time.sleep(2)
        display_summary(player)
        exit()

    pirate_pool = [
        Pirate("Sneaky Bandit", "Raider", 1, [("Rusty Blade", 5)], 20, 100),
        Pirate("Forest Raider", "Scout", 2, [("Dagger", 6)], 30, 300),
        Pirate("River Marauder", "Warrior", 3, [("Trident", 10)], 50, 500),
    ]

    pirate = random.choice(pirate_pool)
    print(f"A pirate appears! {pirate.name} ({pirate.pirate_type}) is ready to fight!")
    time.sleep(1)

    fighter_ship = player.ships["FighterShip"]

    while pirate.health > 0 and fighter_ship.health > 0:
        print(f"\nYour ship's health: {fighter_ship.health}")
        print(f"{pirate.name}'s health: {pirate.health}")
        print(f"Your ship's fuel: {fighter_ship.fuel}")

        if fighter_ship.fuel <= 0:
            print("You have no fuel to continue fighting. The game ends.")
            time.sleep(2)
            display_summary(player)
            exit()

        print("\nChoose your weapon for the attack:")
        for idx, weapon in enumerate(fighter_ship.weapons.keys(), 1):
            stats = fighter_ship.weapons[weapon]
            print(
                f"{idx}. {weapon} (Damage: {stats['damage']}, Fuel Cost: {stats['fuel_cost']})"
            )

        weapon_choice = int(
            choice(
                scene="weapon",
                prompt=f"Choose a weapon (1-{len(fighter_ship.weapons)}): ",
                options=[str(i) for i in range(1, len(fighter_ship.weapons) + 1)],
            )
        )
        weapon_name = list(fighter_ship.weapons.keys())[weapon_choice - 1]

        attack_result = fighter_ship.attack(pirate, weapon_name)
        print(attack_result)

        if pirate.health <= 0:
            print(f"You defeated {pirate.name}! Congratulations.")
            player.credits += pirate.reward
            print(
                f"You earned {pirate.reward} credits! Total credits: {player.credits}"
            )
            time.sleep(2)
            clear_screen()
            return

        pirate_attack = pirate.attack()
        fighter_ship.health -= pirate_attack["damage"]
        print(
            f"{pirate.name} attacks with {pirate_attack['weapon']} and deals {pirate_attack['damage']} damage!"
        )

        if fighter_ship.health <= 0:
            print(f"{fighter_ship.name} has been destroyed! Game over.")
            time.sleep(2)
            clear_screen()
            return


def explore_planet(player, planet_num):
    if player.ships["FighterShip"].fuel <= 0:
        print("You are out of fuel and cannot travel to another planet!")
        time.sleep(2)
        display_summary(player)
        exit()

    planet_options = {
        "1": Planet(
            name="Mercantara",
            level_req=1,
            takes_fuel=10,
            takes_time=1,
            description="A bustling trade hub with various goods.",
            inventory=mercantara_inventory,
        ),
        "2": Planet(
            name="Barteron",
            level_req=2,
            takes_fuel=25,
            takes_time=3,
            description="A planet known for its rare resources.",
            inventory=barteron_inventory,
        ),
        "3": Planet(
            name="Voltrade",
            level_req=3,
            takes_fuel=40,
            takes_time=5,
            description="A high-tech marketplace for elite traders.",
            inventory=voltrade_inventory,
        ),
    }

    planet = planet_options.get(planet_num)
    if not planet:
        print("Invalid planet number!")
        return

    print(planet.display_description())

    if player.ships["FighterShip"].fuel < planet.takes_fuel:
        print("Not enough fuel to travel to this planet!")
        time.sleep(2)
        display_summary(player)
        exit()

    player.ships["FighterShip"].fuel -= planet.takes_fuel
    player.days_passed += planet.takes_time

    print(
        f"You traveled to {planet.name}. It took {planet.takes_time} day(s)\n"
        f"Total days passed: {player.days_passed}\n"
        f"Remaining fuel: {player.ships['FighterShip'].fuel}\n"
    )

    action = choice(
        scene="planet",
        prompt="Do you want to (1) Buy/Sell or (2) Leave?",
        options=["1", "2"],
    )

    if action == "1":
        print(planet.display())
        trade_action = choice(
            scene="trade",
            prompt="Do you want to (1) Buy or (2) Sell?",
            options=["1", "2"],
        )

        if trade_action == "1":
            item_index = int(input("Enter item number to buy: ")) - 1
            quantity = int(input("Enter quantity: "))
            print(planet.buy(player, item_index, quantity))
        elif trade_action == "2":
            item_name = input("Enter item name to sell: ")
            quantity = int(input("Enter quantity: "))
            print(planet.sell(player, item_name, quantity))

    elif action == "2":
        print(f"You decide to leave {planet.name}.")

    if random.random() < 0.4:
        encounter_pirate(player)


def check_goal(player):
    if player.credits >= 2000:
        print(f"\n🎉 Congratulations, {player.name}! You've earned 2000 credits!")
        print(f"Total credits earned: {player.credits}")
        print(f"Days passed: {player.days_passed}")
        print("Thank you for playing!")
        exit()


def display_summary(player):
    print("\nGame Summary:")
    print(f"Total days passed: {player.days_passed}")
    print(f"Total credits earned: {player.credits}")
    if player.credits < 2000:
        print("You didn't achieve the goal of earning 2000 credits.")
        print("Better luck next time!")
    print("Thank you for playing!")


def run():
    clear_screen()
    start()

    player_name = input("Enter your player's name: ").strip()
    while not player_name:
        print("Player name can't be empty. Please enter a valid name.")
        player_name = input("Enter your player's name: ").strip()

    cargo_name = input("Enter your CargoShip's name: ").strip()
    while not cargo_name:
        print("CargoShip name can't be empty. Please enter a valid name.")
        cargo_name = input("Enter your CargoShip's name: ").strip()

    fighter_name = input("Enter your FighterShip's name: ").strip()
    while not fighter_name:
        print("FighterShip name can't be empty. Please enter a valid name.")
        fighter_name = input("Enter your FighterShip's name: ").strip()

    player = Player(name=player_name)
    player.ships["CargoShip"].name = cargo_name
    player.ships["FighterShip"].name = fighter_name

    print(f"\nWelcome, {player.name}! Your ships are ready:")
    print(f"- CargoShip: {cargo_name}")
    print(f"- FighterShip: {fighter_name}")
    time.sleep(2)

    clear_screen()

    while True:
        cmd = choice(
            scene="main",
            prompt="What will you do?\n1. Rest\n2. Travel",
            options=["1", "2"],
        )
        if cmd == "1":
            player.days_passed += 1

            for ship in player.ships.values():
                if hasattr(ship, "fuel"):
                    ship.fuel = ship.max_fuel

            print(
                "You decide to rest. Fuel has been fully recovered for all applicable ships!"
            )
            print(f"One day has passed. Total days passed: {player.days_passed}")

            print(f"Remaining fuel: {player.ships['FighterShip'].fuel}\n")

            if player.health < 100:
                print("\nYou have lost some health.")
                print("Health recovery items available in your inventory:")
                recovery_items = {
                    name: details
                    for name, details in player.inventory.items()
                    if "healing" in details
                }

                if not recovery_items:
                    print("No recovery items available. Consider buying some.")
                else:
                    while player.health < 100:
                        for idx, (name, details) in enumerate(
                            recovery_items.items(), 1
                        ):
                            print(
                                f"{idx}. {name} - Healing: {details['healing']} (x{details['quantity']})"
                            )
                        print("Type 'exit' to stop using recovery items.")

                        item_choice = input(
                            "\nEnter the name of the item you want to use: "
                        ).strip()
                        if item_choice.lower() == "exit":
                            break
                        recovery_result = player.recover_health(item_choice)
                        print(recovery_result)

                        if player.health == 100:
                            print("Your health is now fully recovered!")
                            break

            time.sleep(2)
            clear_screen()
            
        elif cmd == "2":
            print("You decide to travel.")
            clear_screen()
            planet_choice = choice(
                scene="travel",
                prompt="Choose a planet:\n1. Mercantara\n2. Barteron\n3. Voltrade",
                options=["1", "2", "3"],
            )
            explore_planet(player, planet_choice)

        check_goal(player)

        continue_game = choice(
            scene="continue",
            prompt="Do you want to continue? (y/n): ",
            options=["y", "n"],
        )
        if continue_game.lower() != "y":
            display_summary(player)
            break
        time.sleep(2)
        clear_screen()


if __name__ == "__main__":
    run()
