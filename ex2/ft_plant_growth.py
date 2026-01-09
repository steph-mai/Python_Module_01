#!/usr/bin/env python3

class Plant:
    def __init__(self, name, height, current_age):
        self.name = name
        self.height = height
        self.current_age = current_age

    def grow(self, size):
        self.height += size

    def age(self):
        self.current_age += 1

    def get_info(self):
        return f"{self.name}: {self.height}cm, {self.current_age} days old"


def ft_plant_growth():
    plant1 = Plant("Rose", 25, 30)
    plant2 = Plant("Sunflower", 80, 45)

    plants = [plant1, plant2]

    for p in plants:
        print(f"Simulation for {p.name}")
        print("=== Day 1 ===")
        print(p.get_info())
        size_start = p.height
        day = 0
        while (day < 6):
            p.grow(1)
            p.age()
            day += 1
        print("=== Day 7 ===")
        print(p.get_info())
        growth = p.height - size_start
        print(f"Growth this week: +{growth}cm")


if __name__ == "__main__":
    ft_plant_growth()
