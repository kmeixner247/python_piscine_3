from S1E7 import Baratheon, Lannister


class King(Baratheon, Lannister):
    """Wait is he Baratheon or a Lannister?

Inherits from:
    - Baratheon
    - Lannister

Attributes:
    - From Character:
        - first_name (str): The first name of the character.
        - is_alive (bool, optional): Whether the character is alive or not. \
Defaults to True.
    - From Baratheon:
        - family_name (str): The family name of the character, defaults to \
Baratheon.
        - eyes (str): The eye color of the character, defaults to brown.
        - hairs (str): The hair color of the character, defaults to dark.
    - From Lannister:
        - None, as Baratheon is the first inherited class and Lannister \
does not have any attributes that Baratheon doesn't have

Methods:
    - set_eyes(self, color): setter for the eyes attribute
    - set_hairs(self, color): setter for the hairs attribute
    - get_eyes(self, color): getter for the eyes attribute
    - get_hairs(self, color): getter for the hairs attribute
"""
    def set_eyes(self, color):
        """Setter function for eyes

Args:
    - color (str): eye color to be set

Returns:
    None
"""
        self.eyes = color

    def set_hairs(self, color):
        """Setter function for hairs

Args:
    - color (str): hair color to be set

Returns:
    None
"""
        self.hairs = color

    def get_eyes(self):
        """Getter function for the eye color

Returns:
    The eye color as string
"""
        return self.eyes

    def get_hairs(self):
        """Getter function for the hair color

Returns:
    The hair color as string
"""
        return self.hairs
