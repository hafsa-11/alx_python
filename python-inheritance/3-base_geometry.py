"""
This module provides a base geometry class.
"""

class BaseGeometry:
    """
    An empty class representing base geometry.
    """

    def __str__(self):
        """
        Override the __str__ method to customize the string representation.
        """
        return "BaseGeometry()"

# Example usage
bg = BaseGeometry()
print(bg)