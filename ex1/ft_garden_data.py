#!/usr/bin/env python3

class Plant:
    def __init__(self, name, height, current_age):
        self.name = name
        self.height = height
        self.current_age = current_age


def ft_garden_data():
    plant1 = Plant("Rose", 25, 30)
    plant2 = Plant("Sunflower", 80, 45)
    plant3 = Plant("Cactus", 15, 120)

    print("=== Garden Plant Registy ===")
    for p in [plant1, plant2, plant3]:
        print(f"{p.name}: {p.height}cm, {p.current_age} days old")


if __name__ == "__main__":
    ft_garden_data()
