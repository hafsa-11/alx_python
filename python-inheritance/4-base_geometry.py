"""4-base_geometry module

This module defines the BaseGeometry class.
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

if __name__ == "__main__":
    BaseGeometry = __import__('4-base_geometry').BaseGeometry

    bg = BaseGeometry()

    try:
        print(bg.area())
    except Exception as e:
        print("[{}] {}".format(e.__class__.__name__, e))

        raise Exception("area() is not implemented")

if __name__ == "__main__":
    bg = BaseGeometry()

    print(dir(bg))