class Plant:
    """Create a blueprint for plants."""

    def __init__(self, name: str, height: int, age: int) -> None:
        """Initialize a plant with a name, a height and an age."""
        self.name = name
        self.height = height
        self.age = age
        self.final_growth = 0

    def grow(self, size: int) -> None:
        """Give a plant ability to grow."""
        self.height += size
        self.final_growth += size
            
    def get_type(self) -> str:
        """Define the plant type"""
        return "regular"
    
    def display_info(self) -> None:
        """Display plant data."""
        print(f"- {self.name}: "
              f"{self.height}cm,")

    
class FloweringPlant(Plant):
    """Create a specialized plant with floral characteristics."""

    def __init__(self, name: str, height: int, age: int, color: str) -> None:
        """Initialize a flowering plant with an additionnal color attribute."""
        super().__init__(name, height, age)
        self.color = color
 
    def get_type(self) -> str:
        """Define the plant type"""
        return "flowering"
    
    def display_info(self) -> None:
        """Display flowering plant data."""
        print(f"- {self.name}: "
              f"{self.height}cm, "
              f"{self.color} flowers (blooming)")


class PrizeFlower(FloweringPlant):
    """Create a specialized type of flowering plant eligible for competition prizes."""

    def __init__(self, name: str, height: int, age: int, color: str, prize: int) -> None:
        """Initialize prize-winning flower with its competition score."""
        super().__init__(name, height, age, color)
        self.prize = prize

    def win_prize(self) -> None:
        """Display the competition prize points earned by the flower."""
        print(f"Prize points: {self.prize}")
    
    def get_type(self) -> str:
        """Define the plant type"""
        return "prize"
    
    def display_info(self) -> None:
        """Display prize flowering plant data."""
        print(f"- {self.name}: "
              f"{self.height}cm, "
              f"{self.color} flowers (blooming), "
              f"Prize points: {self.prize}")


class GardenManager:
    """Create a garden manager, which creates gardens and statistics."""

    def __init__(self, garden_name: str) -> None:
        """Initialize garden manager and its internal analytics helper."""
        self.garden_name = garden_name
        self.plants = []
        self.stats_helper = self.GardenStats()
    
    class GardenStats:
        """Nested class helper to calculate analytics."""

        def display_report(self, garden_name: str, plants: list):
            """Display analytics report."""

            print(f"=== {garden_name}'s Garden Report ===")
            print("Plants in garden")
            for p in plants:
                p.display_info()

            total_plants = 0
            total_growth = 0
            counts = {"regular": 0, "flowering": 0, "prize": 0}

            for p in plants:
                total_plants += 1
                ptype = p.get_type()
                if ptype in counts:
                    counts[ptype] += 1
                total_growth += p.final_growth
            
            print(f"Plants added: {total_plants}, "
                  f"Total growth: {total_growth}")
            print(f"Plant types: {counts['regular']} regular, "
                  f"{counts['flowering']} flowering, "
                  f"{counts['prize']} prize flowers")
        
    def show_analytics(self) -> None:
        self.stats_helper.display_report(self.garden_name, self.plants)

    @classmethod
    def create_garden_network(cls, names: list) -> list:
        """Initialize a list of manager and dsplay the gardens number"""
        gardens_number = 0
        for name in names:
            gardens_number += 1
        print(f"Total gardens managed: {gardens_number}")
        return [cls(name) for name in names]

    @staticmethod
    def height_validation_test(height: int) -> bool:
        return height > 0
    
    @staticmethod

            
                  
            
            

