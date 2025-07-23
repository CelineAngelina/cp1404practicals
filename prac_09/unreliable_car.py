import random
from prac_09.car import Car

class UnreliableCar(Car):
    """Specialised version of a UnreliableCar, depending on reliability."""
    def __init__(self, name, fuel, reliability):
        """Initialise an UnreliableCar with name, fuel, and reliability."""
        super().__init__(name, fuel)
        self.reliability = reliability

    def drive(self, distance):
        """Attempt to drive based on reliability."""
        random_number = random.randint(0,100)
        if random_number >= self.reliability:
            return 0
        return super().drive(distance)