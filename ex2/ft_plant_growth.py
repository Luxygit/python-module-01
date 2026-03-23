"""This subject asks to affect the state of plants with operations"""


class Plant:
    """Single plant construct"""
    def __init__(self, name: str, cms: float, days: int, rate: float) -> None:
        """Initialising plant instance"""
        self.name = name
        self.cms = cms
        self.days = days
        self.rate = rate

    def grow(self) -> None:
        """Calculates added cm's"""
        self.cms += self.rate

    def age(self) -> None:
        """calculates added age"""
        self.days += 1

    def show(self) -> str:
        """Display plant info method"""
        return f"{self.name}: {round(self.cms, 1)}cm, {self.days} days old"


def sim_week(plant: Plant) -> None:
    "simulates a week of growth with a range for loop"
    start_cms = plant.cms
    for day in range(1, 8):
        print(f"=== Day {day} ===")
        print(f"{plant.show()}")
        plant.grow()
        plant.age()
    total_increase = plant.cms - start_cms
    print(f"Growth this week: {round(total_increase)}cm")


def main() -> None:
    """Creating plant objects and displaying modified info"""
    print("=== Garden Plant Growth ===")
    rose = Plant("Rose", 25.0, 30, 0.8)
    sim_week(rose)


if __name__ == "__main__":
    main()
