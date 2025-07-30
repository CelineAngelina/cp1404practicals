from prac_09.taxi import Taxi

class SilverServiceTaxi(Taxi):
    """Specialised version of a SilverServiceTaxi, with fanciness and a flagfall charge."""
    flagfall = 4.50

    def __init__(self, name, fuel, fanciness = float):
        """Initialise a SilverServiceTaxi with name, fuel, and fanciness."""
        super().__init__(name, fuel)
        self.fanciness = fanciness
        self.price_per_km = Taxi.price_per_km * fanciness

    def get_fare(self):
        """Return the price for the silver service taxi trip."""
        return super().get_fare() + self.flagfall

    def __str__(self):
        """Return a string like a Taxi but with flagfall."""
        return f"{super().__str__()} plus flagfall of ${self.flagfall}"