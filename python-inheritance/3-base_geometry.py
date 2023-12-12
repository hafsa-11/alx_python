"""
This module provides a base geometry class.
"""

class BaseGeometry:
    """
    An empty class representing base geometry.
    """

    def __dir__(self):
        """
        Override the __dir__ method to exclude the default attributes and methods.
        """
        return []