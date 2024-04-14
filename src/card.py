class Card:

    def __init__(self, number: str, opacity: str, color: str, shape: str) -> None:
        """Initializes the card attributes."""
        self.number = number
        self.opacity = opacity
        self.color = color
        self.shape = shape

    def __repr__(self) -> str:
        """Prints a representation of the card."""
        return f"Card(number={self.number}, opacity={self.opacity}, color={self.color}, shape={self.shape})"
    
    def __str__(self) -> str:
        """Prints a readable string describing the card."""
        string = f"{self.number} {self.opacity} {self.color} {self.shape}"
        if self.number != "1":
            string += "s"
        return string

    def __eq__(self, other: object) -> bool:
        """Determines if another object is equal to this card."""
        return isinstance(other, Card) and \
               self.number == other.number and \
               self.opacity == other.opacity and \
               self.color == other.color and \
               self.shape == other.shape
