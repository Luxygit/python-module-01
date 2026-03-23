"""This subject is about data validation and encapsulation"""


class Plant:
    """secure plant class validating data"""
    def __init__(self, name: str, height: float, age: int) -> None:
        """initialising with defaults in case of invalid inputs"""
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

    def get_height(self) -> float:
        """returns validated height"""
        return self._height

    def get_age(self) -> int:
        """returns validated age"""
        return self._age

    def show(self) -> str:
        """returns the last valid values"""
        return f"{self.name}: {round(self._height, 1)}cm, {self._age} days old"


def main() -> None:
    """initializes object and then tries to modify values"""
    print("=== Garden Security System ===")
    rose = Plant("Rose", 15.0, 10)
    print(f"Plant created: {rose.show()}\n")
    rose.set_height(25.0)
    print(f"Height updated: {round(rose.get_height())}cm")
    rose.set_age(30)
    print(f"Age updated: {rose.get_age()} days\n")
    rose.set_height(-10)
    rose.set_age(-5)
    print(f"\nCurrent state: {rose.show()}")


if __name__ == "__main__":
    main()
