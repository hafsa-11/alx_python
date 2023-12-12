"""
This module provides a base geometry class.
"""

class BaseGeometry:
    """
    An empty class representing base geometry.
    """
    pass

    def __dir__(self):
        """
        Override the __dir__ method to exclude the default attributes and methods.
        """
        return ['__doc__', '__module__']

# Example usage
print(dir(BaseGeometry))