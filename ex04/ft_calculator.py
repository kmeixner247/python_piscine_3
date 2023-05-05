class calculator:
    @staticmethod
    def dotproduct(V1: list[float], V2: list[float]) -> None:
        dot = sum([a*b for (a, b) in zip(V1, V2)])
        print(f"Dot product is {dot}")

    @staticmethod
    def add_vec(V1: list[float], V2: list[float]) -> None:
        sum = [float(a+b) for (a, b) in zip(V1, V2)]
        print(f"Add Vector is {sum}")

    @staticmethod
    def sous_vec(V1: list[float], V2: list[float]) -> None:
        sub = [float(a-b) for (a, b) in zip(V1, V2)]
        print(f"Add Vector is {sub}")
