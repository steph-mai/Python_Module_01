class Plant:
    def __init__(self, name, height, age):
        self.name = name
        self.height = height
        self.age = age

class Flower(Plant):
    def __init__(self, name, height, age, color):
        super().__init__(self, name, height, age)
        self.color = color
    
    def bloom(self):
        print(f"{self.name} is blooming beautifuly!")

class Tree(Plant):
    def __init__(self, name, height, age, trunk_diameter):
        super().__init__(self, name, height, age)
        self.trunk_diameter = trunk_diameter
    
    def produce_shade(self, aera):
        print(f"{self.name} provides {aera} square meters of shade")