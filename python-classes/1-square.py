class Square:
    """
    This class represents a square.

    Attributes:
        __size (int): The size of the square.
    """

    def _init_(self, size=0):
        """
        Initializes a new Square instance.

        Args:
            size (int, optional): The size of the square. Defaults to 0.
        """
        if not isinstance(size, int):
            raise TypeError("size must be an integer")

        if size < 0:
            raise ValueError("size must be >= 0")

        self.__size = size

if _name_ == "_main_":
    # Example of using the Square class
    my_square_1 = Square(3)
    print(type(my_square_1))
    print(my_square_1._dict_)

    my_square_2 = Square()
    print(type(my_square_2))
    print(my_square_2._dict_)

    try:
        print(my_square_1.size)
    except Exception as e:
        print(e)

    try:
        print(my_square_1.__size)
    except Exception as e:
        print(e)

    try:
        my_square_3 = Square("3")
        print(type(my_square_3))
        print(my_square_3._dict_)
    except Exception as e:
        print(e)

    try:
        my_square_4 = Square(-89)
        print(type(my_square_4))
        print(my_square_4._dict_)
    except Exception as e:
        print(e)