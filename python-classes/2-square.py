"""
Module: 2-square

This module defines the Square class, representing a square by its size.
"""

class Square:
    """
    This is the Square class that defines a square by its size.
    """

    def _init_(self, size=0):
        """
        Initializes a new Square instance.

        Parameters:
        - size (int, optional): The size of the square. Defaults to 0.
        """
        if not isinstance(size, int):
            raise TypeError("size must be an integer")

        if size < 0:
            raise ValueError("size must be >= 0")

        self.__size = size

    def area(self):
        """
        Computes and returns the area of the square.

        Returns:
        - int: The area of the square.
        """
        return self.__size ** 2


# Test case 1
mysquare = Square(3)
print("{}".format(mysquare.area()))  # Output: 9

# Test case 2
mysquare = Square(89)
print("{}".format(mysquare.area()))  # Output: 7921

# Test case 3
mysquare = Square()
print("{}".format(mysquare.area()))  # Output: 0