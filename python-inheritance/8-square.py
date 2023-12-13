"""8-square module

This module defines the Square class.
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

class Square(Rectangle):
    """Square class

    This class inherits from Rectangle and represents a square.
    """

    def __init__(self, size):
        """Initialize a Square instance.

        Args:
            size (int): The size of the square.
        """
        self.integer_validator("size", size)
        super().__init__(size, size)

    def __str__(self):
        """Return a string representation of the square.

        Returns:
            str: A string in the format [Rectangle] <size>/<size>
        """
        return "[Square] {}/{}".format(self._Rectangle__width, self._Rectangle__height)

if __name__ == "__main__":
    Square = __import__('8-square').Square

    s = Square(13)

    print(s)
    print(s.area())