"""7-rectangle module

This module defines the Rectangle class.
"""

class BaseGeometry:
    """BaseGeometry class

    This class serves as the base class for geometry-related classes.
    """

    def area(self):
        """Public instance method that raises an Exception.

        Raises:
            Exception: Always raises an Exception with the message
                "area() is not implemented".
        """
        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        """Validate the value parameter.

        Args:
            name (str): The name of the parameter.
            value (int): The value to be validated.

        Raises:
            TypeError: If value is not an integer.
            ValueError: If value is less than or equal to 0.
        """
        if not isinstance(value, int):
            raise TypeError("{} must be an integer".format(name))
        if value <= 0:
            raise ValueError("{} must be greater than 0".format(name))

class Rectangle(BaseGeometry):
    """Rectangle class

    This class inherits from BaseGeometry and represents a rectangle.
    """

    def __init__(self, width, height):
        """Initialize a Rectangle instance.

        Args:
            width (int): The width of the rectangle.
            height (int): The height of the rectangle.
        """
        self.integer_validator("width", width)
        self.integer_validator("height", height)
        self.__width = width
        self.__height = height

    def area(self):
        """Calculate and return the area of the rectangle."""
        return self.__width * self.__height

    def __str__(self):
        """Return a string representation of the rectangle.

        Returns:
            str: A string in the format [Rectangle] <width>/<height>
        """
        return "[Rectangle] {}/{}".format(self.__width, self.__height)

if __name__ == "__main__":
    Rectangle = __import__('7-rectangle').Rectangle

    r = Rectangle(3, 5)

    print(r)
    print(r.area())