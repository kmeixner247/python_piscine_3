from S1E9 import Character


class Baratheon(Character):
    """Representing the Baratheon family."""
    def __init__(self, first_name, is_alive=True):
        super().__init__(first_name, is_alive)
        self.family_name = "Baratheon"
        self.eyes = "brown"
        self.hairs = "dark"

    def __str__(self):
        return f"Vector: ('{self.family_name}', '{self.hairs}', '{self.eyes}')"

    def __repr__(self):
        return f"Vector: ('{self.family_name}', '{self.hairs}', '{self.eyes}')"

    def die(self):
        self.is_alive = False


class Lannister(Character):
    """Representing the Lannister family."""
    def __init__(self, first_name, is_alive=True):
        super().__init__(first_name, is_alive)
        self.family_name = "Lannister"
        self.eyes = "blue"
        self.hairs = "light"

    def __str__(self):
        return f"Vector: ('{self.family_name}', '{self.hairs}', '{self.eyes}')"

    def __repr__(self):
        return f"Vector: ('{self.family_name}', '{self.hairs}', '{self.eyes}')"

    def die(self):
        self.is_alive = False

    def create_lannister(first_name: str, is_alive=True):
        return Lannister(first_name, is_alive)
