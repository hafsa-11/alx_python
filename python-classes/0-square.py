#!/usr/bin/python3
"""
This module defines a Square class.

The Square class has a private instance attribute 'size'.
"""

class Square:
    """
    This class represents a square.

    Attributes:
        __size (int): The size of the square.
    """

    def _init_(self, size):
        """
        Initializes a new Square instance.

        Args:
            size (int): The size of the square.
        """
        self.__size = size

if _name_ == "_main_":
    # Example of using the Square class
    my_square = Square(3)
    print(type(my_square))
    print(my_square._dict_)

    try:
        print(my_square.size)
    except Exception as e:
        print(e)

    try:
        print(my_square.__size)
    except Exception as e:
        print(e)