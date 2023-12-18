#!/usr/bin/python3
"""Module defining the Square class."""
from models.rectangle import Rectangle

class Square(Rectangle):
    """The Square class, inherits from Rectangle."""

    def __init__(self, size, x=0, y=0, id=None):
        """Initialize the Square instance.

        Args:
            size (int): Size of the square.
            x (int): X-coordinate of the square.
            y (int): Y-coordinate of the square.
            id (int): If provided, assign it to the public instance attribute id.
                      Otherwise, let the super class handle it.
        """
        super().__init__(size, size, x, y, id)

    def __str__(self):
        """Return a string representation of the square."""
        return "[Square] ({}) {}/{} - {}".format(
            self.id, self.x, self.y, self.width
        )
