class Band:
    """Band class."""
    def __init__(self, name):
        """Construct a Band with a name and empty musicians' collection."""
        self.name = name
        self.musicians = []

    def __str__(self):
        """Return a string consisting band's name and list of musicians."""
        return f"{self.name} ({', '.join(str(musician) for musician in self.musicians)})"

    def add(self, musician):
        """Add a Musician to band's collection."""
        self.musicians.append(musician)

    def play(self):
        """Return a string showing each musician playing (or needing) an instrument."""
        return '\n'.join(musician.play() for musician in self.musicians)