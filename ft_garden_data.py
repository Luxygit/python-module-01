"""
Garden Plant data display by using a class
to streamline the plant creation
"""


class Plant:
    """Single plant construct"""
    def __init__(self, name: str, height: int, age: int) -> None:
        """Initialising plant instance"""
        self.name = name
        self.height = height
        self.age = age

    def display(self) -> None:
        """Display plant info method"""
        print(f"{self.name}: {self.height}cm, {self.age} days old")


def main() -> None:
    """Main function creates plant objects and calls display"""
    print("=== Garden Plant Registry ===")
    rose = Plant("Rose", 25, 30)
    sunflower = Plant("Sunflower", 80, 45)
    cactus = Plant("Cactus", 15, 120)
    rose.display()
    sunflower.display()
    cactus.display()


if __name__ == "__main__":
    main()
