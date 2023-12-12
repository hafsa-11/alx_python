"""
This module provides a base geometry class.
"""

class BaseGeometry:
    """
    An empty class representing base geometry.
    """

    @classmethod
    def __dir__(cls):
        """
        Override the __dir__ method to exclude the default attributes and methods.
        """
        return []

# Example usage
bg = BaseGeometry()
print(dir(bg))
print(dir(BaseGeometry))