class Plant:
    """Create blueprint for plants."""

    def __init__(self, name: str, height: int, age: int) -> None:
        """Initialize plant with name, height and age"""
        self.name = name
        self.height = height
        self.age = age


def ft_plant_factory(data: tuple) -> Plant:
    """Create a plant from a tuple of data."""
    return Plant(*data)


def ft_plant_manager() -> None:
    """Ask the factory to create a plant and display data."""
    data_plants: list[tuple] = [
        ("Rose", 25, 30),
        ("Oak", 200, 365),
        ("Cactus", 5, 90),
        ("Sunflower", 80, 45),
        ("Fern", 15, 120)
    ]

    total_plants: int = 0
    print("=== Plant Factory Output ===")

    for data in data_plants:
        new_plant: Plant = ft_plant_factory(data)
        print(f"Created: {new_plant.name} "
              f"({new_plant.height}cm,"
              f" {new_plant.age} days)")
        total_plants += 1

    print()
    print(f"Total plants created: {total_plants}")


if __name__ == "__main__":
    ft_plant_manager()
