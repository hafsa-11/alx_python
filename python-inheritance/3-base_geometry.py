"""3-base_geometry module

This module defines the BaseGeometry class.
"""

class BaseGeometry:
    """Empty BaseGeometry class

    This class serves as the base class for geometry-related classes.
    It is currently empty and intended for further development.
    """

    def __dir__(self):
        """Custom implementation for dir().

        Returns:
            list: List of attributes for dir() to display.
        """
        return ['__class__', '__dict__', '__dir__', '__doc__', '__module__']

bg = BaseGeometry()
print(dir(bg))
print(dir(BaseGeometry))