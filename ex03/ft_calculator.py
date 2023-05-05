class calculator:
    """A calculator class that can be initialized with a vector arbitrary \
length and supports in-place addition, subtraction, multiplication and \
division.

    Attributes:
        - vector (list): the internally stored vector. Initialized at creation.

    Methods:
        - __init__(self, vector: list) -> None: Constructor.
        - __add__(self, object) -> None: Addition with scalar.
        - __mul__(self, object) -> None: Multiplication with scalar.
        - __sub__(self, object) -> None: Subtraction with scalar.
        - __truediv__(self, object) -> None: Division with scalar.
"""

    def __init__(self, vector: list):
        """Constructor of the calculator class.

    Args:
        - vector (list): The initialization vector
"""
        self.vector = vector

    def __add__(self, object) -> None:
        """In-place addition of vector with a scalar. Adds the scalar to \
every element of the vector and prints the result.

    Args:
        - object (float | int): The scalar to be added
"""
        self.vector = [n + object for n in self.vector]
        print(self.vector)

    def __mul__(self, object) -> None:
        """In-place multiplication of vector with a scalar. Multiplies \
every element of the vector with the scalar and prints the result.

    Args:
        - object (float | int): The scalar to multiply the vector with
"""
        self.vector = [n * object for n in self.vector]
        print(self.vector)

    def __sub__(self, object) -> None:
        """In-place subtraction of vector with a scalar. Subtracts a scalar \
from every element of the vector and prints the result.

    Args:
        - object (float | int): The scalar to subtracted from the vector
"""
        """In-place subtraction of vector with a scalar. Subtracts a scalar \
from every element of the vector and prints the result.

    Args:
        - object (float | int): The scalar to subtracted from the vector
"""
        self.vector = [n - object for n in self.vector]
        print(self.vector)

    def __truediv__(self, object) -> None:
        """In-place division of vector with a scalar. Divides every element \
of the vector by a scalar and prints the result.

    Args:
        - object (float | int): The scalar to divide the vector by
"""
        try:
            self.vector = [n / object for n in self.vector]
            print(self.vector)
        except ZeroDivisionError as msg:
            print(f"calculator: ZeroDivisionError: {msg}")
