class SecurePlant:
    def __init__(self, name, height=0, age=0):
        self.name = name
        self._height = height
        self._age = age
    
    def get_height(self):
        return self._height
    
    def get_age(self):
        return self._age
        
    def set_height(self, val):
        if val < 0:
            print(f"\nInvalid operation attempted: height {val}cm [REJECTED]")
            print("Security : Negative height rejected\n")
        else:
            self._height = val
            print(f"Height updated: {self._height}cm [OK]")
    
    def set_age(self, val):
        if val < 0:
            print(f"\nInvalid operation attempted: age {val} days [REJECTED]")
            print("Security : Negative age rejected\n")
        else:
            self._age = val
            print(f"Age updated: {self._age} days [OK]")
    
def ft_garden_security():
    print("=== Garden Security System ===")
    new_plant = SecurePlant("Rose", 0, 0)
    print(f"Plant created: {new_plant.name}")
    new_plant.set_height(25)
    new_plant.set_age(30)
    new_plant.set_height(-5)
    print(f"Current plant: {new_plant.name} ({new_plant.get_height()}cm, {new_plant.get_age()} days)")


if __name__ == "__main__":
    ft_garden_security()