"""Implemented class methods and static methods"""


class Plant:
    """Base class for plants"""
    def __init__(self, name: str, height: int) -> None:
        """Initialises common data"""
        self.name = name
        self.height = height

    def grow(self) -> None:
        "instance method adds height"
        self.height += 1
        print(f"{self.name} grew 1cm")

    def get_info(self) -> str:
        """displays common data"""
        return f"{self.name}: {self.height}cm"


class FloweringPlant(Plant):
    """specific type of plant with colors"""
    def __init__(self, name: str, height: int, color: str) -> None:
        """calls parent and adds color"""
        super().__init__(name, height)
        self.color = color

    def get_info(self) -> str:
        """displays extra plant type data"""
        base = super().get_info()
        return f"{base}, {self.color} flowers (blooming)"


class PrizeFlower(FloweringPlant):
    """specific type of plant with points and color"""
    def __init__(self, name: str, height: int, color: str, pts: int) -> None:
        """calls FloweringPlant and adds points"""
        super().__init__(name, height, color)
        self.points = pts

    def get_info(self) -> str:
        """extends FloweringPlant info"""
        base = super().get_info()
        return f"{base}, Prize points: {self.points}"


class GardenManager:
    """
    Plant collection and stats, using class variables and
    class methods operate on the class itself not the instance
    static methods dont need class/instance data
    nested classes help hide logic outside where it's needed
    """
    total_gardens = 0

    class GardenStats:
        """Nested helper for stats, just does maths, doesnt care about self."""
        @staticmethod
        def calculate_score(plants_count: int, total_height: int) -> int:
            """calcs garden score"""
            return (plants_count * total_height)

    def __init__(self, owner: str) -> None:
        """initialising manager for one owner"""
        self.owner = owner
        self.plants = []
        self.total_growth = 0
        self.p_count = 0
        self.reg_count = 0
        self.flow_count = 0
        self.prize_count = 0
        GardenManager.total_gardens += 1

    def add_plant(self, plant: Plant, p_type: str) -> None:
        """adds one plant to collection"""
        self.plants = self.plants + [plant]
        self.p_count += 1
        if p_type == "regular":
            self.reg_count += 1
        if p_type == "flowering":
            self.flow_count += 1
        if p_type == "prize":
            self.prize_count += 1
        print(f"Added {plant.name} to {self.owner}'s garden")

    def help_growth(self) -> None:
        """makes all plants in the garden grow"""
        print(f"\n{self.owner} is helping all plants grow...")
        for i in range(self.p_count):
            plant = self.plants[i]
            plant.grow()
            self.total_growth += 1

    @classmethod
    def create_garden_network(cls, names: list) -> list:
        """
        method to create multiple managers at once
        grabs names from a list and adds them to the network
        through the GardenManager.owner
        """
        network = []
        for name in names:
            new_garden = cls(name)
            network = network + [new_garden]
        return network

    @staticmethod
    def validate_height(height: int) -> bool:
        """util to check if height is positive"""
        return height > 0


def main() -> None:
    """displays all stats"""
    print("=== Garden Management System Demo ===\n")
    gardens = GardenManager.create_garden_network(["Alice", "Bob"])
    alice_g = gardens[0]
    oak = Plant("Oak Tree", 100)
    rose = FloweringPlant("Rose", 25, "red")
    sun = PrizeFlower("Sunflower", 50, "yellow", 10)
    alice_g.add_plant(oak, "regular")
    alice_g.add_plant(rose, "flowering")
    alice_g.add_plant(sun, "prize")
    alice_g.help_growth()
    total_h = 0
    for i in range(alice_g.p_count):
        total_h += alice_g.plants[i].height
    print(f"\n=== {alice_g.owner}'s Garden Report ===")
    print("Plants in garden:")
    for i in range(alice_g.p_count):
        p = alice_g.plants[i]
        print(f"- {p.get_info()}")
    total_h = oak.height + rose.height + sun.height
    alice_score = alice_g.GardenStats.calculate_score(alice_g.p_count, total_h)
    bob_score = gardens[1].GardenStats.calculate_score(3, 20)
    print(f"\nPlants added: {alice_g.p_count}, "
          f"Total growth: {alice_g.total_growth}cm")
    print(f"Plant types: {alice_g.reg_count} regular, "
          f"{alice_g.flow_count} flowering, "
          f"{alice_g.prize_count} prize flowers")
    print(f"\nHeight validation test: {GardenManager.validate_height(100)}")
    print(f"Garden scores - Alice: {alice_score}, Bob: {bob_score}")
    print(f"Total gardens managed: {GardenManager.total_gardens}")


if __name__ == "__main__":
    main()
