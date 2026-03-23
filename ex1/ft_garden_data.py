"""
Garden Plant data display by using a class
to streamline the plant creation
"""


class Plant:
    """Single plant construct"""
    def __init__(self, name: str, cms: int, days: int) -> None:
        """Initialising plant instance"""
        self.name = name
        self.cms = cms
        self.days = days

    def show(self) -> str:
        """returns plant info method"""
        return f"{self.name}: {self.cms}cm, {self.days} days old"


def main() -> None:
    """Main function creates plant objects and calls display"""
    print("=== Garden Plant Registry ===")
    rose = Plant("Rose", 25, 30)
    sunflower = Plant("Sunflower", 80, 45)
    cactus = Plant("Cactus", 15, 120)
    print(f"{rose.show()}")
    print(f"{sunflower.show()}")
    print(f"{cactus.show()}")


if __name__ == "__main__":
    main()
