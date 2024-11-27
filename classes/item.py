class Item:
    """
    Base class for all items in the game.
    """
    def __init__(self, name, description, price):
        self.name = name
        self.description = description
        self.price = price

    def get_details(self):
        """
        Returns the details of the item as a dictionary.
        """
        return {
            "name": self.name,
            "description": self.description,
            "price": self.price
        }


class Medicine(Item):
    """
    Subclass for medicine items.
    """
    def __init__(self, name, description, price, healing):
        super().__init__(name, description, price)
        self.healing = healing

    def get_details(self):
        details = super().get_details()
        details["healing"] = self.healing
        return details


class Clothing(Item):
    """
    Subclass for clothing items.
    """
    def __init__(self, name, description, price, defense_bonus):
        super().__init__(name, description, price)
        self.defense_bonus = defense_bonus

    def get_details(self):
        details = super().get_details()
        details["defense_bonus"] = self.defense_bonus
        return details


class Food(Item):
    """
    Subclass for food and provisions.
    """
    def __init__(self, name, description, price, strength_boost):
        super().__init__(name, description, price)
        self.strength_boost = strength_boost

    def get_details(self):
        details = super().get_details()
        details["strength_boost"] = self.strength_boost
        return details


class PetCompanion(Item):
    """
    Subclass for pet companions.
    """
    def __init__(self, name, description, price, effect):
        super().__init__(name, description, price)
        self.effect = effect

    def get_details(self):
        details = super().get_details()
        details["effect"] = self.effect
        return details


# Example Usage
if __name__ == "__main__":
    # Creating Medicine Items
    bandages = Medicine("Bandages", "Basic wound wraps for small injuries.", 10, 10)
    first_aid_kit = Medicine("First Aid Kit", "A compact kit with essential tools for healing.", 50, 20)

    # Creating Clothing Items
    space_suit = Clothing("Basic Space Suit", "Standard-issue, no frills.", 50, 5)
    thermal_cloak = Clothing("Thermal Insulated Cloak", "Keeps you safe in harsh environments.", 200, 15)

    # Creating Food Items
    protein_bar = Food("Protein Bar", "Compact and nutritious.", 10, 5)
    exotic_cuisine = Food("Exotic Alien Cuisine", "Rare dishes from distant worlds.", 150, 30)

    # Creating Pet Companion Items
    astro_kitten = PetCompanion("Astro-Kitten", "Cute companion for morale.", 30, "+2 morale boost")
    quantum_hound = PetCompanion("Quantum Hound", "Tracks rare loot during exploration.", 700, "+15% rare loot detection")

    # Displaying Item Details
    print(bandages.get_details())
    print(space_suit.get_details())
    print(protein_bar.get_details())
    print(astro_kitten.get_details())

