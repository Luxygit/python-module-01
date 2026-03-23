"""Streamlining the creation of plants looping with range()"""


class Plant:
    """Initialising plant construct"""
    def __init__(self, name: str, cms: float, days: int) -> None:
        """Initialising plant instance"""
        self.name = name
        self.cms = cms
        self.days = days

    def show(self) -> str:
        "returns plant info"
        return f"{self.name}: {round(self.cms, 1)}cm, {self.days} days old"


def main() -> None:
    """Creating plant objects from a data list"""
    plants = [
        Plant("Rose", 25.0, 30),
        Plant("Oak", 200.0, 365),
        Plant("Cactus", 5.0, 90),
        Plant("Sunflower", 80.0, 45),
        Plant("Fern", 15.0, 120)
    ]
    print("=== Plant Factory Output ===")
    for i in range(1, 5):
        print(f"Created: {plants[i].show()}")


if __name__ == "__main__":
    main()
