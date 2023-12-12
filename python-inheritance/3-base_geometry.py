"""
This module provides a base geometry class.
"""

class BaseGeometry:
    """
    An empty class representing base geometry.
    """

    def __repr__(self):
        """
        Override the __repr__ method to customize the representation.
        """
        return "<{} object at {}>".format(self.__class__.__name__, hex(id(self)))

# Example usage
bg = BaseGeometry()
print(bg)