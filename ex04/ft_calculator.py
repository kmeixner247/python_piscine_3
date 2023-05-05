class calculator:
    """A calculator class that does not need to be initialized and only \
contains three static methods, which can be used to compute vectors with each \
other.

    Attributes:
        None

    Methods:
        - dotproduct(V1: list[float], V2: list[float]) -> None:
            Static method to calculate the dotproduct of two vectors.
        - add_vec(V1: list[float], V2: list[float]) -> None:
            Static method to add two vectors together.
        - sous_vec(V1: list[float], V2: list[float]) -> None:
            Weirdly french named static method to subtract one vector from \
another
"""
    @staticmethod
    def dotproduct(V1: list[float], V2: list[float]) -> None:
        """Static method to calculate the dotproduct of two vectors.\
 Prints the result.

The dotproduct is defined as the sum of the product of all coordinate pairs \
of the two vectors.

For example, the dotproduct of the vectors (2, 5) and (7, 3) would be \
(2 * 7, 5 * 3) = (14, 15)

    Args:
        - V1 (list): The first vector in form of a list
        - V2 (list): The second vector in form of a list

    Returns:
        None
"""
        dot = sum([a*b for (a, b) in zip(V1, V2)])
        print(f"Dot product is: {dot}")

    @staticmethod
    def add_vec(V1: list[float], V2: list[float]) -> None:
        """Static method to add two vectors element by element. \
Prints the result.

For example: (2, 5) + (7, 3) = (2+7, 5+3) = (14, 8)

    Args:
        - V1 (list): The first vector in form of a list
        - V2 (list): The second vector in form of a list

    Returns:
        None
"""
        sum = [float(a+b) for (a, b) in zip(V1, V2)]
        print(f"Add Vector is : {sum}")

    @staticmethod
    def sous_vec(V1: list[float], V2: list[float]) -> None:
        """Static method to add two vectors element by element. Has a french \
name for some reason. Prints the result.

For example: (2, 5) - (7, 3) = (2-7, 5-3) = (-5, 2)

    Args:
        - V1 (list): The first vector in form of a list
        - V2 (list): The second vector in form of a list

    Returns:
        None
"""
        sub = [float(a-b) for (a, b) in zip(V1, V2)]
        print(f"Sous Vector is: {sub}")
