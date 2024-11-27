class Pirate:
    def __init__(self, name, pirate_type, level, weapons, health):
        self.name = name
        self.pirate_type = pirate_type
        self.level = level
        self.weapons = weapons  # List of (weapon_name, damage)
        self.health = health

    def attack(self):
        if not self.weapons:
            return {"action": "attack", "weapon": "No weapon", "damage": 0}
        weapon = self.weapons[0]  # Choose the first weapon for simplicity
        return {"action": "attack", "weapon": weapon[0], "damage": weapon[1]}

    def take_damage(self, damage):
        self.health -= damage
        if self.health > 0:
            return {"status": "alive", "remaining_health": self.health}
        else:
            return {"status": "defeated", "remaining_health": 0}

    def display_stats(self):
        return {
            "name": self.name,
            "type": self.pirate_type,
            "level": self.level,
            "health": self.health,
            "weapons": [{"name": w[0], "damage": w[1]} for w in self.weapons],
        }

# Example Usage for Testing
if __name__ == "__main__":
    # Creating pirates for different regions
    sneaky_bandit = Pirate(
        name="Sneaky Bandit",
        pirate_type="Raider",
        level=1,
        weapons=[("Rusty Blade", 5), ("Basic Laser Pistol", 7)],
        health=20
    )

    big_captain = Pirate(
        name="Big Captain Bloodflame",
        pirate_type="Warlord (Boss)",
        level=10,
        weapons=[("Graviton Cannon", 50), ("Anti-Matter Grenades", 60), ("Void Scythe", 70)],
        health=200
    )

    # Accessing pirate stats
    sneaky_bandit_stats = sneaky_bandit.display_stats()
    big_captain_stats = big_captain.display_stats()

    # Combat example
    player_attack_damage = 15
    combat_response = sneaky_bandit.take_damage(player_attack_damage)
    attack_response = sneaky_bandit.attack()

    # Test outputs for integration
    print(sneaky_bandit_stats)  # To check stats (Example only)
    print(big_captain_stats)  # To check stats (Example only)
    print(combat_response)  # To check combat response (Example only)
    print(attack_response)  # To check attack response (Example only)

