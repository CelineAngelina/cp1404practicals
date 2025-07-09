CURRENT_YEAR = 2025
VINTAGE_AGE = 50

class Guitar:
    """Represent a guitar with name, year, and cost."""
    def __init__(self, name="", year=0, cost=0.0):
        """Initialise a Guitar instance."""
        self.name = name
        self.year = year
        self.cost = cost

    def __str__(self):
        """Return a string representation of the guitar."""
        return f"{self.name:24} ({self.year}) : ${self.cost:>10,.2f}"

    def get_age(self):
        """Return the age of the guitar based on the current year."""
        return CURRENT_YEAR - self.year

    def is_vintage(self):
        """Determine if the guitar is vintage."""
        return self.get_age() >= VINTAGE_AGE

    def __lt__(self, other):
        """Compare one guitar with another based on year."""
        return self.year < other.year

# def run_test():
#     guitar1 = Guitar("Fender Stratocaster", 2014, 765.4)
#     guitar2 = Guitar("Gibson L-5 CES",1922,16035.4)
#     guitar3 = Guitar("Martin Grand J12-16GTE",2015,2199)
#
#     guitars = [guitar1, guitar2, guitar3]
#
#     guitars.sort()
#
#     print("Guitars sorted by year (oldest to newest):")
#     for guitar in guitars:
#         print(guitar.name)
#
# if __name__ == "__main__":
#     run_test()