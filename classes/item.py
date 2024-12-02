class Item:
    def __init__(self, name, description, price):
        self.name = name
        self.description = description
        self.price = price

    def get_details(self):
        return {
            "name": self.name,
            "description": self.description,
            "price": self.price
        }


class Medicine(Item):
    def __init__(self, name, description, price, healing):
        super().__init__(name, description, price)
        self.healing = healing

    def get_details(self):
        details = super().get_details()
        details["healing"] = self.healing
        return details


class Clothing(Item):
    def __init__(self, name, description, price, defense_bonus):
        super().__init__(name, description, price)
        self.defense_bonus = defense_bonus

    def get_details(self):
        details = super().get_details()
        details["defense_bonus"] = self.defense_bonus
        return details


class Food(Item):
    def __init__(self, name, description, price, strength_boost):
        super().__init__(name, description, price)
        self.strength_boost = strength_boost

    def get_details(self):
        details = super().get_details()
        details["strength_boost"] = self.strength_boost
        return details


class PetCompanion(Item):
    def __init__(self, name, description, price, effect):
        super().__init__(name, description, price)
        self.effect = effect

    def get_details(self):
        details = super().get_details()
        details["effect"] = self.effect
        return details