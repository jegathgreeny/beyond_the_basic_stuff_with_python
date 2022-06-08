class WizCoin:
    """Represents the galleon, sicle and knut coins of wizard currency."""

    def __init__(self, galleons, sickles, knuts):
        """Initialize essential attributes."""
        self.galleons = galleons
        self.sickles = sickles
        self.knuts = knuts
        # Note: __init__() methods NEVER have a return statement.

    def value(self):
        """The value (in knuts) of all coins in the Wiz_coin object."""
        return (self.galleons * 17 * 29) + (self.sickles * 29) + (self.knuts)

    def weight(self):
        """Returns the weight of the coins in grams."""
        return (self.galleons * 31.103) + (self.sickles * 11.34) + (self.knuts * 5.0)
