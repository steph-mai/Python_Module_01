class Plant:
    def __init__(self, name, starting_height, starting_age):
        self.name = name
        self.starting_height = starting_height
        self.starting_age = starting_age


def ft_plant_factory():
    data_plants = [
        ("Rose", 25, 30),
        ("Oak", 200, 365),
        ("Cactus", 5, 90),
        ("Sunflower", 80, 45),
        ("Fern", 15, 120)
    ]

    total_plants = 0

    for data in data_plants:
        new_plant = Plant(data[0], data[1], data[2])
        print(f"Created: {new_plant.name} "
              f"({new_plant.starting_height}cm,"
              f" {new_plant.starting_age} days)")
        total_plants += 1
    print()
    print(f"Total plants created: {total_plants}")


if __name__ == "__main__":
    ft_plant_factory()
