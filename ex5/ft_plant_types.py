"""Class inheritance among plants"""


class Plant:
    """Base class for all plants"""
    def __init__(self, name: str, height: float, age: int) -> None:
        """initialising common plant data"""
        self.name = name
        self._height = 0.0
        self._age = 0
        self.set_height(height)
        self.set_age(age)

    def set_height(self, height: float) -> None:
        """updates height value or displays error"""
        if height >= 0:
            self._height = height
        else:
            print(f"{self.name}: Error, height can't be negative")
            print("Height update rejected")

    def set_age(self, age: int) -> None:
        """updates age value or displays error"""
        if age >= 0:
            self._age = age
        else:
            print(f"{self.name}: Error, age can't be negative")
            print("Age update rejected")

    def show(self) -> str:
        """returns the class data"""
        return f"{self.name}: {round(self._height, 1)}cm, {self._age} days old"


class Flower(Plant):
    """Specific plant type"""
    def __init__(self, name: str, h: float, a: int, color: str) -> None:
        """calls parent and adds data"""
        super().__init__(name, h, a)
        self.color = color

    def bloom(self) -> None:
        """specific method"""
        print(f"[asking the {self.name.lower()} to bloom]\n"
              f"{self.show()}"
              f"\n {self.name} is blooming beautifully!\n")

    def show(self) -> str:
        """returns common and extended type data"""
        return (f"{super().show()} \n Color: {self.color}")


class Tree(Plant):
    """Specific plant type"""
    def __init__(self, name: str, h: float, a: int, diameter: float) -> None:
        """calls parent init and adds specific data"""
        super().__init__(name, h, a)
        self.trunk_diameter = diameter

    def produce_shade(self) -> None:
        """specific method for this type of plant"""
        print(f"[asking the {self.name.lower()} to produce shade]"
              f"\nTree {self.name} now produces a shade of "
              f"{self._height}cm long and {self.trunk_diameter}cm wide.\n")

    def show(self) -> str:
        """returns common and extended type data"""
        return (f"{super().show()} \n Trunk diameter: {self.trunk_diameter}cm")


class Vegetable(Plant):
    """Specific plant type"""
    def __init__(self, n: str, h: float, a: int, ssn: str, ntr: int) -> None:
        """Calls parent init and adds specific data"""
        super().__init__(n, h, a)
        self.harvest_season = ssn
        self.nutritional_value = ntr

    def show(self) -> str:
        """returns common and extended type data"""
        return (f"{super().show()}"
                f"\n Harvest season: {self.harvest_season}"
                f"\n Nutritional value: {self.nutritional_value}")

    def age(self) -> None:
        """updates age"""
        self.set_age(self._age + 20)

    def grow(self) -> None:
        """updates height"""
        self.set_height(self._height + 42)

    def grow_age(self) -> None:
        """calls the data modifiers and updates nutri value"""
        self.age()
        self.grow()
        self.nutritional_value += 20
        print(f"[make {self.name.lower()} grow and age for 20 days]")
        print(f"{self.show()}")


def main() -> None:
    """Instantiates specific plants"""
    print("=== Garden Plant Types ===")
    print("=== Flower")
    rose = Flower("Rose", 15.0, 10, "red")
    print(f"{rose.show()}"
          f"\n {rose.name} has not bloomed yet")
    rose.bloom()
    print("=== Tree")
    oak = Tree("Oak", 200.0, 365, 5.0)
    print(f"{oak.show()}")
    oak.produce_shade()
    print("=== Vegetable")
    tomato = Vegetable("Tomato", 5.0, 10, "April", 0)
    print(f"{tomato.show()}")
    tomato.grow_age()


if __name__ == "__main__":
    main()
