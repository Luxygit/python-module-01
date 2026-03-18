
"""This subject asks to affect the state of plants with operations"""


class Plant:
    """Single plant construct"""
    def __init__(self, name: str, cms: int, days: int) -> None:
        """Initialising plant instance"""
        self.name = name
        self.cms = cms
        self.days = days

    def get_info(self) -> None:
        """Display plant info method"""
        print(f"{self.name}: {self.cms}cm, {self.days} days old")

    def grow(self) -> None:
        """Calculates added cm's"""
        self.cms = self.cms + 6

    def age(self) -> None:
        """calculates added age"""
        self.days = self.days + 6


def main() -> None:
    """Creating plant objects and displaying modified info"""
    print("=== Day 1 ===")
    rose = Plant("Rose", 25, 30)
    rose.get_info()
    print("=== Day 7 ===")
    rose.grow()
    rose.age()
    rose.get_info()
    print("Growth this week: +6cm\n")
    print("=== Day 1 ===")
    sunflower = Plant("Sunflower", 80, 65)
    sunflower.get_info()
    print("=== Day 7 ===")
    sunflower.grow()
    sunflower.age()
    sunflower.get_info()
    print("Growth this week: +6cm\n")
    print("=== Day 1 ===")
    cactus = Plant("Cactus", 15, 120)
    cactus.get_info()
    print("=== Day 7 ===")
    cactus.grow()
    cactus.age()
    cactus.get_info()
    print("Growth this week: +6cm")


if __name__ == "__main__":
    main()
