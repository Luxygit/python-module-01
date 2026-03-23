"""Implemented class methods and static methods"""


class Plant:
    """
    Plant collection and stats, using
    class methods operate on the class itself not the instance
    static methods dont need class/instance data
    nested classes help hide logic outside where it's needed
    """
    class Analytics:
        """nested class to hold stat methods"""
        def __init__(self) -> None:
            """Initialises values"""
            self._grow_calls = 0
            self._age_calls = 0
            self._show_calls = 0

        def increment_grow(self) -> None:
            "counts grow() calls"
            self._grow_calls += 1

        def increment_age(self) -> None:
            """counts age() calls"""
            self._age_calls += 1

        def increment_show(self) -> None:
            """counts show() calls"""
            self._show_calls += 1

        def display(self) -> None:
            """displays age grow show number of calls"""
            print(f"Stats: {self._grow_calls} grow, "
                  f"{self._age_calls} age, {self._show_calls} show")

    def __init__(self, name: str, height: float, age: int) -> None:
        """initialises common validated plant data and analytics"""
        self.name = name
        self._height = 0.0
        self._age = 0
        self.stats = self.Analytics()
        self.set_height(height)
        self.set_age(age)

    @staticmethod
    def is_older_than_year(age: int) -> bool:
        """checks if age is greater than 365"""
        return age > 365

    @classmethod
    def create_anonymous(cls) -> 'Plant':
        """creates plant with defeault unknown values"""
        return cls("Unknown plant", 0.0, 0)

    def set_height(self, height: float) -> None:
        """validates height or displays error"""
        if height >= 0:
            self._height = height
        else:
            print(f"{self.name}: Error, height can't be negative")
            print("Height update rejected")

    def set_age(self, age: int) -> None:
        """validates age or displays error"""
        if age >= 0:
            self._age = age
        else:
            print(f"{self.name}: Error, age can't be negative")
            print("Age update rejected")

    def grow(self, amount: float) -> None:
        """sets height and keeps record of calls"""
        self.set_height(self._height + amount)
        self.stats.increment_grow()

    def age(self) -> None:
        """set age and keeps record of calls"""
        self.set_age(self._age + 20)
        self.stats.increment_age()

    def show(self) -> str:
        """returns plant data and increments show calls"""
        self.stats.increment_show()
        return f"{self.name}: {round(self._height, 1)}cm, {self._age} days old"

    def get_extra_stats(self) -> None:
        """placeholder method, does nothing unless plant is a tree"""
        pass


class Flower(Plant):
    """specific type class"""
    def __init__(self, name: str, height: float, age: int, color: str) -> None:
        super().__init__(name, height, age)
        self._color = color
        self._is_blooming = False

    def bloom(self) -> None:
        """flower can bloom"""
        self._is_blooming = True

    def show(self) -> str:
        """returns extended stat info"""
        if self._is_blooming:
            return (f"{super().show()}\n Color: {self._color}"
                    f"\n {self.name} is blooming beautifully!")
        else:
            return (f"{super().show()}\n Color: {self._color}"
                    f"\n {self.name} has not bloomed yet")


class Seed(Flower):
    """class tracks seed count after blooming"""
    def __init__(self, name: str, height: float, age: int, color: str) -> None:
        """initialises plant type plus seed count"""
        super().__init__(name, height, age, color)
        self._seeds = 0

    def produce_seeds(self, count: int) -> None:
        """set seeds count if flower is blooming"""
        if self._is_blooming:
            self._seeds = count

    def show(self) -> str:
        """returns seed type specific extended data"""
        return f"{super().show()}\n Seeds: {self._seeds}"


class Tree(Plant):
    """class with shade tracking"""
    def __init__(self, name: str, height: float, age: int, dim: float) -> None:
        """initialising child and parent class"""
        super().__init__(name, height, age)
        self._trunk_diameter = dim
        self._shade_calls = 0

    def produce_shade(self) -> None:
        """track shade"""
        self._shade_calls += 1
        print("[asking the oak to produce shade]")
        print(f"Tree {self.name} now produces a shade of "
              f"{round(self._height, 1)}cm long and "
              f"{round(self._trunk_diameter, 1)}cm wide.")

    def get_extra_stats(self) -> None:
        """tree specific data"""
        print(f" {self._shade_calls} shade")

    def show(self) -> str:
        """returns specific tree type stats"""
        return (f"{super().show()}\n Trunk diameter: "
                f"{round(self._trunk_diameter, 1)}cm")


def display_stats(plant: Plant) -> None:
    """displays stats for any type"""
    print(f"[statistics for {plant.name}]")
    plant.stats.display()
    plant.get_extra_stats()


def main() -> None:
    """displays and calls all info"""
    print("=== Garden statistics ===")
    print("=== Check year-old")
    print(f"Is 30 days more than a year? -> {Plant.is_older_than_year(30)}")
    print(f"Is 400 days more than a year? -> {Plant.is_older_than_year(400)}")
    print("\n=== Flower")
    rose = Flower("Rose", 15.0, 10, "red")
    print(rose.show())
    display_stats(rose)
    rose.grow(8.0)
    print(f"[asking the {rose.name.lower()} to grow and bloom]")
    rose.bloom()
    print(rose.show())
    display_stats(rose)

    print("\n=== Tree")
    oak = Tree("Oak", 200.0, 365, 5.0)
    print(oak.show())
    display_stats(oak)
    oak.produce_shade()
    display_stats(oak)

    print("\n=== Seed")
    sun = Seed("Sunflower", 80.0, 45, "yellow")
    print(sun.show())
    print(f"[make {sun.name.lower()} grow, age and bloom]")
    sun.age()
    sun.grow(30.0)
    sun.bloom()
    sun.produce_seeds(42)
    print(sun.show())
    display_stats(sun)

    print("\n=== Anonymous")
    anon = Plant.create_anonymous()
    print(anon.show())
    display_stats(anon)


if __name__ == "__main__":
    main()
