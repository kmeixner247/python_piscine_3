from abc import ABC, abstractmethod


class Character(ABC):
    """Abstract class representing a character.

    Inherits from:
        - ABC

    Attributes:
        - first_name (str): The first name of the character.
        - is_alive (bool, optional): Whether the character is alive or not. \
Defaults to True.

    Methods:
        - __init__(self, first_name: str, is_alive=True): Constructor
        - die(self): Abstract method, must be implemented in subclasses
"""
    def __init__(self, first_name: str, is_alive=True):
        """Constructor of class Character.

    Args:
        - first_name (str): The first name of the character.
        - is_alive (bool, optional): Whether the character is alive or not. \
Defaults to True.
"""
        self.first_name = first_name
        self.is_alive = is_alive

    @abstractmethod
    def die(self):
        """Abstract method, must be implemented in subclasses"""
        pass


class Stark(Character):
    """Subclass representing a character from the Stark family.

    Inherits from:
        - Character

    Methods:
        - die(self): Method to change the health state of the character to ded.
"""
    def die(self):
        """Method to change the health state of the character to dead."""
        self.is_alive = False
