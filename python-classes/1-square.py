#!/usr/bin/python3
"""Module documentation"""

class Square:
    """Square class"""

    def _init_(self, size=0):
        """Initialize the Square instance"""
        if not isinstance(size, int):
            raise TypeError("size must be an integer")
        elif size < 0:
            raise ValueError("size must be >= 0")
        self.__size = size