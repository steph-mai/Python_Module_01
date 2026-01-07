#!/usr/bin/env python3

class Plant:
    def __init__(self, name, height, age):
        self.name = name
        self.height = height
        self.age = age


def ft_garden_data():
    plant1 = Plant("rose", 25, 30)
    plant2 = Plant("Sunflower", 80, 45)
    plant3 = Plant("cactus", 15, 120)

    print("=== Garden Plant Registy ===")
    for p in [plant1, plant2, plant3]:
        print(f"{p.name.capitalize()}: {p.height}cm, {p.age} days old")


if __name__ == "__main__":
    ft_garden_data()
