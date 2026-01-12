class Plant:
    def __init__(self, name, height, age):
        self.name = name
        self.height = height
        self.age = age

class Flower(Plant):
    def __init__(self, name, height, age, color):
        super().__init__(name, height, age)
        self.color = color
    
    def bloom(self):
        print(f"{self.name} is blooming beautifully!")

class Tree(Plant):
    def __init__(self, name, height, age, trunk_diameter):
        super().__init__(name, height, age)
        self.trunk_diameter = trunk_diameter
    
    def produce_shade(self, area):
        print(f"{self.name} provides {area} square meters of shade")

class Vegetable(Plant):
    def __init__(self, name, height, age, harvest_season):
        super().__init__(name, height, age)
        self.harvest_season = harvest_season
    
    def nourish(self):
        print(f"{self.name} is rich in vitamin C")

def plant_types():
    print("=== Garden Plant Types ===")
    print()
    data_plants = [
        (Flower, "Rose", 25, 30, "red"),
        (Flower, "Pivoine", 30, 20, "purple"),
        (Tree, "Oak", 500, 1825, 50),
        (Tree, "Poplar", 300, 365, 45),
        (Vegetable, "Tomato", 80, 90, "summer"),
        (Vegetable, "Cucumber", 30, 80, "summer")
    ]

    for data in data_plants:
        plant_class = data[0]
        args = data[1:]
        new_plant = plant_class(*args)

        if plant_class == Flower:
            print(f"{new_plant.name} (Flower): {new_plant.height}cm, {new_plant.age} days, {new_plant.color} color")
            new_plant.bloom()
            print()

        if plant_class == Tree:
            print(f"{new_plant.name} (Tree): {new_plant.height}cm, {new_plant.age} days, {new_plant.trunk_diameter}cm diameter")
            new_plant.produce_shade(78)
            print()
    
        if plant_class == Vegetable:
            print(f"{new_plant.name} (Vegetable): {new_plant.height}cm, {new_plant.age} days, {new_plant.harvest_season} harvest")
            new_plant.nourish()
            print()

if __name__ == "__main__":
    plant_types()


        
