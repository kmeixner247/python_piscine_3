from S1E9 import Character


class Baratheon(Character):
    """Representing the Baratheon family.

    Inherits from:
        - Character

    Attributes:
        - from Character:
            - first_name (str): The first name of the character.
            - is_alive (bool, optional): Whether the character is alive or \
not. Defaults to True.
        - family_name (str): The family name of the character, defaults to \
Baratheon.
        - eyes (str): The eye color of the character, defaults to brown.
        - hairs (str): The hair color of the character, defaults to dark.

    Methods:
        - __init__(self, first_name, is_alive=True): Constructor.
        - __str__(self): 'Dunder' method, returns a string representation.
        - __repr__(self): 'Dunder' method, returns an string representation.
        - die(self): Method to change the health state of the character to \
dead.
"""
    def __init__(self, first_name, is_alive=True):
        """Constructor of class Baratheon. Calls the constructor of the \
Character base class with the arguments and sets the following default values:
    - family_name: Baratheon
    - eyes: brown
    - hairs: dark

    Args:
        - first_name (str): The first name of the character.
        - is_alive (bool, optional): Whether the character is alive or not. \
Defaults to True.
"""
        super().__init__(first_name, is_alive)
        self.family_name = "Baratheon"
        self.eyes = "brown"
        self.hairs = "dark"

    def __str__(self):
        """'Dunder' method for Baratheon. Returns a string representation in a \
readable format."""
        return f"({self.first_name} {self.family_name}, alive: {self.is_alive}\
            ,{self.hairs} hairs, {self.eyes} eyes)"

    def __repr__(self):
        """'Dunder' method for Baratheon. This is the format that is asked for \
in the subject for no reason. As far as I understand, the proper one would be:

return f"Baratheon('{self.first_name}', {self.is_alive})

because it's supposed to be usable to recreate the object"""
        return f"Vector: ('{self.family_name}', '{self.eyes}', '{self.hairs}')"

    def die(self):
        """Method to change the health state of the character to dead."""
        self.is_alive = False


class Lannister(Character):
    """Representing the Lannister family.

    Inherits from:
        - Character

    Attributes:
        - from Character:
            - first_name (str): The first name of the character.
            - is_alive (bool, optional): Whether the character is alive or \
not. Defaults to True.
        - family_name (str): The family name of the character, defaults to \
Lannister.
        - eyes (str): The eye color of the character, defaults to blue.
        - hairs (str): The hair color of the character, defaults to light.

    Methods:
        - __init__(self, first_name, is_alive=True): Constructor.
        - __str__(self): 'Dunder' method, returns a string representation.
        - __repr__(self): 'Dunder' method, returns an string representation.
        - die(self): Method to change the health state of the character to \
dead.
"""
    def __init__(self, first_name, is_alive=True):
        """Constructor of class Lannister. Calls the constructor of the \
Character base class with the arguments and sets the following default values:
    - family_name: Lannister
    - eyes: blue
    - hairs: light

    Args:
        - first_name (str): The first name of the character.
        - is_alive (bool, optional): Whether the character is alive or not. \
Defaults to True.
"""
        super().__init__(first_name, is_alive)
        self.family_name = "Lannister"
        self.eyes = "blue"
        self.hairs = "light"

    def __str__(self):
        """'Dunder' method for Lannister. Returns a string representation in a \
readable format."""
        return f"({self.first_name} {self.family_name}, alive: {self.is_alive}\
            ,{self.hairs} hairs, {self.eyes} eyes)"

    def __repr__(self):
        """'Dunder' method for Lannister. This is the format that is asked for \
in the subject for no reason. As far as I understand, the proper one would be:

return f"Lannister('{self.first_name}', {self.is_alive})

because it's supposed to be usable to recreate the object"""
        return f"Vector: ('{self.family_name}', '{self.eyes}', '{self.hairs}')"

    def die(self):
        """Method to change the health state of the character to dead."""
        self.is_alive = False

    @staticmethod
    def create_lannister(first_name: str, is_alive=True):
        """Static method. Create a new Lannister character with the given \
name and alive state.

    Args:
        - first_name (str): The first name of the character.
        - is_alive (bool, optional): Whether the character is alive or not. \
Defaults to True.

    Returns:
        Lannister: A new Lannister character object.
"""
        return Lannister(first_name, is_alive)
