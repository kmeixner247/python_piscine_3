class calculator:
    def __init__(self, vector: list):
        self.vector = vector
    def __add__(self, object) -> None:
        self.vector = [n + object for n in self.vector]
        print(self.vector)
    def __mul__(self, object) -> None:
        self.vector = [n * object for n in self.vector]
        print(self.vector)
    def __sub__(self, object) -> None:
        self.vector = [n - object for n in self.vector]
        print(self.vector)
    def __truediv__(self, object) -> None:
        try:
            self.vector = [n / object for n in self.vector]
            print(self.vector)
        except ZeroDivisionError as msg:
            print(f"calculator: ZeroDivisionError: {msg}")
