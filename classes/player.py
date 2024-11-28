from planet import Fight_Planet
from pirate import Pirate
from ship import Ship, CargoShip, FighterShip     
class Player:
    def __init__(self, name):
        self.name = name
        self.level = 1
        self.credits = 100
        self.health = 100
        self.inventory = {
            "Rusty Blade": {"damage": 5, "price": 15},
            "Basic Laser Pistol": {"damage": 7, "price": 30},
            "Basic First Aid Kit": {"healing": 10, "price": 50},
        }
        self.ships = {
            "CargoShip": CargoShip(5),
            "FighterShip": FighterShip(
                name="Basic Fighter", weapons=["Laser Gun"]
            )
        }
        
    def display_stats(self):
        return {
            "Name": self.name,
            "Level": self.level,
            "Health": self.health,
            "Money": self.credits,
            "Inventory": self.inventory,
            "Ships": self.ships,
        }
 #This part can be changed later on as we decided player's inventory is actually cargo_space   
    def add_to_inventory(self, item_name, quantity):
        self.inventory[item_name] = self.inventory.get(item_name, 0) + quantity
    
    def remove_from_inventory(self, item_name, quantity):
        if self.inventory.get(item_name, 0) < quantity:
            raise ValueError(f"Not enough {item_name} to remove. Available: {self.inventory.get(item_name, 0)}")
        self.inventory[item_name] -= quantity
        if self.inventory[item_name] == 0:
            del self.inventory[item_name]
    
#Fight on land
    def fight(self, fight_planet, region_index, pirate_index):
      region = fight_planet.get_region(region_index)
      if not region:
        print("Invalid region selection.")
        return
    
      pirate = fight_planet.choose_pirate(region_index, pirate_index)
      if not isinstance(pirate, Pirate):
        print("Invalid pirate selection.")
        return

      print(f"You are fighting {pirate.name} (Level: {pirate.level}, Health: {pirate.health})")

      while pirate.health > 0 and self.health > 0:
        print("\nYour Health:", self.health)
        print("Pirate's Health:", pirate.health)

        # Choose an action
        print("\nChoose your action:")
        print("1. Attack")
        print("2. Maneuver")
        print("3. Give Up")
        choice = input("> ")

        if choice == "1":  # Attack
            # Player chooses weapon
            print("Choose your weapon:")
            for idx, weapon in enumerate(self.inventory.get("weapons", [])):
                print(f"{idx + 1}. {weapon['name']} (Damage: {weapon['damage']})")

            weapon_choice = int(input("> ")) - 1
            if 0 <= weapon_choice < len(self.inventory["weapons"]):
                weapon = self.inventory["weapons"][weapon_choice]
                pirate_damage = weapon["damage"]
                pirate.take_damage(pirate_damage)
                print(f"You attacked with {weapon['name']} dealing {pirate_damage} damage.")

                # Pirate counterattacks
                pirate_attack = pirate.attack()
                self.health -= pirate_attack["damage"]
                print(
                    f"The pirate counterattacks with {pirate_attack['weapon']} dealing {pirate_attack['damage']} damage."
                )
            else:
                print("Invalid weapon choice.")

        elif choice == "2":  # Maneuver
            print("You successfully maneuvered, avoiding damage!")

        elif choice == "3":  # Give Up
            print("You gave up and left the fight.")
            return

        else:
            print("Invalid action. Please choose again.")

        # Check if the pirate is defeated
        if pirate.health <= 0:
            print(f"You defeated {pirate.name}!")
            loot = pirate.weapons
            self.inventory.setdefault("weapons", []).extend(loot)
            print(f"You looted the pirate's weapons: {', '.join(w[0] for w in loot)}.")
            break

        # Check if the player is defeated
        if self.health <= 0:
            print("You have been defeated. Better luck next time!")
            return

    print("\nReturning to region selection...")
