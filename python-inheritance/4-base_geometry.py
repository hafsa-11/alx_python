class BaseGeometry:
    """
    A base geometry class.
    """

    def area(self):
        """
        Public instance method that raises an Exception with the message "area() is not implemented".
        """
        raise Exception("area() is not implemented")

try:
    BaseGeometry = __import__('4-base_geometry').BaseGeometry

    bg = BaseGeometry()

    try:
        print(bg.area())
    except Exception as e:
        print("[{}] {}".format(e.__class__.__name__, e))
except ImportError:
    print("Error importing BaseGeometry from '4-base_geometry'")