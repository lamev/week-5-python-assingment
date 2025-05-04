# Assignment 1: Design Your Own Class! 
class Superhero:
    """Base class for all superheroes"""
    
    def __init__(self, name, secret_identity, powers, weakness):
        self.name = name
        self._secret_identity = secret_identity  # Protected attribute
        self.powers = powers
        self.__weakness = weakness  # Private attribute
        
    def introduce(self):
        print(f"I am {self.name}! My powers include: {', '.join(self.powers)}")
        
    def reveal_secret(self):
        print(f"My real identity is {self._secret_identity}")
        
    def get_weakness(self):
        return self.__weakness
    
    def use_power(self):
        print(f"{self.name} uses {self.powers[0]}!")


class FlyingSuperhero(Superhero):
    """Specialized class for flying heroes"""
    
    def __init__(self, name, secret_identity, powers, weakness, max_altitude):
        super().__init__(name, secret_identity, powers, weakness)
        self.max_altitude = max_altitude
        
    def fly(self):
        print(f"{self.name} soars at {self.max_altitude} feet!")
        
    def use_power(self):  # Override parent method
        print(f"{self.name} takes to the skies using {self.powers[0]}!")


class TechSuperhero(Superhero):
    """Specialized class for tech-based heroes"""
    
    def __init__(self, name, secret_identity, powers, weakness, gadgets):
        super().__init__(name, secret_identity, powers, weakness)
        self.gadgets = gadgets
        
    def use_gadget(self):
        print(f"{self.name} deploys {self.gadgets[0]}!")
        
    def use_power(self):  # Override parent method
        print(f"{self.name} activates their {self.powers[0]} technology!")


# Create instances
superman = FlyingSuperhero(
    name="Superman",
    secret_identity="Clark Kent",
    powers=["flight", "super strength", "heat vision"],
    weakness="Kryptonite",
    max_altitude=50000
)

iron_man = TechSuperhero(
    name="Iron Man",
    secret_identity="Tony Stark",
    powers=["repulsor beams", "AI systems"],
    weakness="Electromagnetic pulses",
    gadgets=["arc reactor", "J.A.R.V.I.S"]
)

# Demonstrate functionality
superman.introduce()
superman.fly()
superman.use_power()

iron_man.introduce()
iron_man.use_gadget()
iron_man.use_power()

# Demonstrate encapsulation
print("\nEncapsulation demonstration:")
print(iron_man.get_weakness())  # Accessing private attribute via method
try:
    print(iron_man.__weakness)  # This will fail
except AttributeError as e:
    print(f"Error: {e}")


    # Activity 2: Polymorphism Challenge!
    class Animal:
    def __init__(self, name):
        self.name = name
        
    def move(self):
        raise NotImplementedError("Subclasses must implement this method")


class Fish(Animal):
    def move(self):
        print(f"{self.name} is swimming! 🐟")


class Bird(Animal):
    def move(self):
        print(f"{self.name} is flying! 🦅")


class Snake(Animal):
    def move(self):
        print(f"{self.name} is slithering! 🐍")


class Kangaroo(Animal):
    def move(self):
        print(f"{self.name} is hopping! 🦘")


# Create a list of animals
animals = [
    Fish("Nemo"),
    Bird("Eagle"),
    Snake("Viper"),
    Kangaroo("Joey")
]

# Demonstrate polymorphism
print("Animal Movement Demonstration:")
for animal in animals:
    animal.move()

# Additional demonstration with different vehicles
print("\nVehicle Movement Demonstration:")

class Vehicle:
    def move(self):
        raise NotImplementedError("Subclasses must implement this method")


class Car(Vehicle):
    def move(self):
        print("Driving on the road! 🚗")


class Boat(Vehicle):
    def move(self):
        print("Sailing on water! ⛵")


class Plane(Vehicle):
    def move(self):
        print("Flying through the air! ✈️")


class Helicopter(Vehicle):
    def move(self):
        print("Hovering in place! 🚁")


vehicles = [Car(), Boat(), Plane(), Helicopter()]

for vehicle in vehicles:
    vehicle.move()