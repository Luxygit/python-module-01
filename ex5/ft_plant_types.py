"""Class inheritance among plants"""


class Plant:
    """Base class for all plants"""
    def __init__(self, name: str, height: int, age: int) -> None:
        """initialising common plant data"""
        self.name = name
        self.height = height
        self.age = age


class Flower(Plant):
    """Specific plant type"""
    def __init__(self, name: str, h: int, a: int, color: str) -> None:
        """calls parent and adds data"""
        super().__init__(name, h, a)
        self.color = color

    def bloom(self) -> None:
        """specific method"""
        print(f"{self.name} is blooming beautifully!")


class Tree(Plant):
    """Specific plant type"""
    def __init__(self, name: str, h: int, a: int, diameter: int) -> None:
        """calls parent init and adds specific data"""
        super().__init__(name, h, a)
        self.trunk_diameter = diameter

    def produce_shade(self) -> None:
        """specific method for this type of plant"""
        shade = self.height * self.trunk_diameter // 100
        print(f"{self.name} provides {shade} square meters of shade")


class Vegetable(Plant):
    """Specific plant type"""
    def __init__(self, name: str, h: int, a: int, ssn: str, ntr: str) -> None:
        """Calls parent init and adds specific data"""
        super().__init__(name, h, a)
        self.harvest_season = ssn
        self.nutritional_value = ntr


def main() -> None:
    """Instantiates specific plants"""
    print("=== Garden Plant Types ===")
    rose = Flower("Rose", 25, 30, "red")
    oak = Tree("Oak", 500, 1825, 50)
    tomato = Vegetable("Tomato", 80, 90, "summer", "vitamin C")
    print(f"\n{rose.name} (Flower): {rose.height}cm, {rose.age} days, "
          f"{rose.color} color")
    rose.bloom()
    print(f"\n{oak.name} (Tree): {oak.height}cm, {oak.age} days, "
          f"{oak.trunk_diameter}cm diameter")
    oak.produce_shade()
    print(f"\n{tomato.name} (Vegetable): {tomato.height}cm, {tomato.age} days,"
          f" {tomato.harvest_season} harvest\n"
          f"{tomato.name} is rich in {tomato.nutritional_value}")


if __name__ == "__main__":
    main()
