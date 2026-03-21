
"""Streamlining the creation of plants using range()"""


class Plant:
    """Initialising plant construct"""
    def __init__(self, name: str, cms: int, days: int) -> None:
        """Initialising plant instance"""
        self.name = name
        self.cms = cms
        self.days = days


def main() -> None:
    """Creating plant objects from a data list"""
    plant_data = [
        ("Rose", 25, 30),
        ("Oak", 200, 365),
        ("Cactus", 5, 90),
        ("Sunflower", 80, 45),
        ("Fern", 15, 120)
    ]
    print("=== Plant Factory Output ===")
    for i in range(5):
        name, height, age = plant_data[i]
        new_plant = Plant(name, height, age)
        print(f"Created: {new_plant.name} "
              f"({new_plant.cms}cm, {new_plant.days} days)")
    print(f"\nTotal plants created: {i + 1}")


if __name__ == "__main__":
    main()
