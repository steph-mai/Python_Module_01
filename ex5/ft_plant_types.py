class Plant:
    """Create a blueprint for secure plants."""

    def __init__(self, name: str, height: int, age: int) -> None:
        """Initialize plant with name, height and age."""
        self.name = name
        self.height = height
        self.age = age

    def execute_action(self) -> None:
        """Placeholder for specialized actions in subclasses"""
        pass

    def display_info(self) -> None:
        """Placeholder for display info in subclasses"""
        pass


class Flower(Plant):
    """Create a specialized type called flower"""

    def __init__(self, name: str, height: int, age: int, color: str) -> None:
        """Initialize flower with name, height, age and color."""
        super().__init__(name, height, age)
        self.color = color

    def bloom(self) -> None:
        """Give flower ability to bloom"""
        print(f"{self.name} is blooming beautifully!")

    def execute_action(self) -> None:
        """execute the specific subclass actions."""
        self.bloom()

    def display_info(self):
        """Display info about the subclass"""
        print(f"{self.name} (Flower): "
              f"{self.height}cm, {self.age} days, "
              f"{self.color} color")


class Tree(Plant):
    """Create a specialized type called tree"""

    def __init__(self, name: str,
                 height: int, age: int,
                 diameter: int) -> None:
        """Initialize tree with name, height, age and trunk diameter."""
        super().__init__(name, height, age)
        self.diameter = diameter

    def produce_shade(self):
        """Calculate the shade in function of the diameter."""
        area: int = int(self.diameter * 1.56)
        print(f"{self.name} provides {area} square meters of shade")

    def execute_action(self) -> None:
        """execute the specific subclass actions."""
        self.produce_shade()

    def display_info(self) -> None:
        """Display tree data."""
        print(f"{self.name} (Tree): {self.height}cm, {self.age} days, "
              f"{self.diameter}cm diameter")


class Vegetable(Plant):
    """Create a specialized type called vegetable"""

    def __init__(self, name: str,
                 height: int, age: int,
                 harvest_season: str) -> None:
        """Initialize vegetable with name, height, age and harvest season."""
        super().__init__(name, height, age)
        self.harvest_season = harvest_season

    def nourish(self):
        """Indicate nutritionnal value"""
        print(f"{self.name} is rich in vitamin C")

    def execute_action(self) -> None:
        """execute the specific subclass actions."""
        self.nourish()

    def display_info(self) -> None:
        """Display vegetable data."""
        print(f"{self.name} (Vegetable): "
              f"{self.height}cm, {self.age} days, "
              f"{self.harvest_season} harvest")


def factory_plant(data: tuple) -> Plant:
    """Create a plant from a tuple of data."""
    plant_class = data[0]
    args = data[1:]
    return plant_class(*args)


def plant_types():
    """Demonstrate polymorphism with different plant types."""
    print("=== Garden Plant Types ===")
    print()
    garden_data = [
        (Flower, "Rose", 25, 30, "red"),
        (Flower, "Peony", 30, 20, "purple"),
        (Tree, "Oak", 500, 1825, 50),
        (Tree, "Poplar", 300, 365, 45),
        (Vegetable, "Tomato", 80, 90, "summer"),
        (Vegetable, "Cucumber", 30, 80, "summer")
    ]

    for data in garden_data:
        new_plant: Plant = factory_plant(data)
        new_plant.display_info()
        new_plant.execute_action()
        print()


if __name__ == "__main__":
    plant_types()
