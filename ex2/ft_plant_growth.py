class Plant:
    """Create blueprint for plants."""

    def __init__(self, name: str, height: int, current_age: int) -> None:
        """Initialize plant with name, height and age"""
        self.name = name
        self.height = height
        self.current_age = current_age

    def grow(self, size: int) -> None:
        """Increase plant height."""
        self.height += size

    def age(self) -> None:
        """Increment plant age."""
        self.current_age += 1

    def get_info(self) -> str:
        """Return informations about a plant"""
        return f"{self.name}: {self.height}cm, {self.current_age} days old"


def ft_plant_growth() -> None:
    """Show plants changing over time"""
    plant1 = Plant("Rose", 25, 30)
    plant2 = Plant("Sunflower", 80, 45)

    plants: list[Plant] = [plant1, plant2]

    for p in plants:
        print(f"Simulation for {p.name}")
        print("=== Day 1 ===")
        print(p.get_info())

        size_start = p.height
        for _ in range(0, 6):
            p.grow(1)
            p.age()

        print("=== Day 7 ===")
        print(p.get_info())
        growth = p.height - size_start
        print(f"Growth this week: +{growth}cm")
        print("\n")


if __name__ == "__main__":
    ft_plant_growth()
