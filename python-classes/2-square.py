class Square:
    """
    This is the Square class that defines a square by its size.
    """

    def _init_(self, size=0):
        """
        Initializes a new Square instance.

        Parameters:
        - size (int, optional): The size of the square. Defaults to 0.
        """
        if not isinstance(size, int):
            raise TypeError("size must be an integer")

        if size < 0:
            raise ValueError("size must be >= 0")

        self.__size = size

    def area(self):
        """
        Computes and returns the area of the square.

        Returns:
        - int: The area of the square.
        """
        return self.__size ** 2