# Base class
class Superhero:
    def __init__(self, name, power, origin):
        self.name = name
        self.power = power
        self.origin = origin
    
    def use_power(self):
        print(f"{self.name} uses {self.power}!")

    def introduce(self):
        print(f"I'm {self.name} from {self.origin} and I fight for justice!")

# Subclass for a specific superhero type
class FlyingHero(Superhero):
    def __init__(self, name, power, origin, flight_speed):
        super().__init__(name, power, origin)
        self.flight_speed = flight_speed

    def use_power(self):
        print(f"{self.name} flies at {self.flight_speed} mph while using {self.power}!")

# Another subclass
class TechHero(Superhero):
    def __init__(self, name, power, origin, suit_version):
        super().__init__(name, power, origin)
        self.suit_version = suit_version

    def use_power(self):
        print(f"{self.name} activates suit version {self.suit_version} to unleash {self.power}!")


hero1 = FlyingHero("SkyWing", "Wind Slash", "Sky City", 500)
hero2 = TechHero("IronCode", "Laser Barrage", "Tech Valley", "v3.2")

hero1.introduce()
hero1.use_power()

hero2.introduce()
hero2.use_power()
