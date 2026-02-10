#!/usr/bin/env python3

class Plant:
    """Create a blueprint for plants with a name, a height and an age."""

    def __init__(self, name: str, height: int, current_age: int) -> None:
        self.name = name
        self.height = height
        self.current_age = current_age


def ft_garden_data() -> None:
    """Display plants data"""
    plant1 = Plant("Rose", 25, 30)
    plant2 = Plant("Sunflower", 80, 45)
    plant3 = Plant("Cactus", 15, 120)

    print("=== Garden Plant Registry ===")
    plants: list[Plant] = [plant1, plant2, plant3]
    for p in plants:
        print(f"{p.name}: {p.height}cm, {p.current_age} days old")


if __name__ == "__main__":
    ft_garden_data()
