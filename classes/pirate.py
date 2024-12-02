class Pirate:
    def __init__(self, name, pirate_type, level, weapons, health, reward):
        self.name = name
        self.pirate_type = pirate_type
        self.level = level
        self.weapons = weapons
        self.health = health
        self.reward = reward

    def attack(self):
        if not self.weapons:
            return {"action": "attack", "weapon": "No weapon", "damage": 0}
        weapon = self.weapons[0]
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