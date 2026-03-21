"""This subject is about data validation and conditionals"""


class SecurePlant:
    def __init__(self, name: str, height: int, age: int) -> None:
        """Creating individual instance values and methods"""
        self.name = name
        self.height = height
        self.age = age

    def get_info(self):
        """displays last valid values"""
        print(f"\nCurrent plant: {self.name}"
              f" ({self.height}cm, {self.age} days)")

    def set_height(self, height: int) -> None:
        """updates height value or displays errork"""
        if height >= 0:
            self.height = height
            self.get_height()
        else:
            print(f"\nInvalid operation attempted: height {height} [REJECTED]")
            print("Security: Negative height rejected")

    def set_age(self, age: int) -> None:
        """updates age value or displays error"""
        if age >= 0:
            self.age = age
            self.get_age()
        else:
            print(f"\nInvalid operation attempted: age {age} [REJECTED]")
            print("Security: Negative age rejected")

    def get_height(self) -> None:
        """displays validated height"""
        if self.height is not None:
            print(f"Height Updated: {self.height}cm [OK]")

    def get_age(self) -> None:
        """displays validated age"""
        if self.age is not None:
            print(f"Age Updated: {self.age} days [OK]")


def main() -> None:
    """initializes object and then tries to modify values"""
    rose = SecurePlant("Rose", 4, 30)
    print("=== Garden Security System ===")
    print(f"Plant created: {rose.name}")
    rose.set_height(-10)
    rose.set_age(-5)
    rose.get_info()


if __name__ == "__main__":
    main()
