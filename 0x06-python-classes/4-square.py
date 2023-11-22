#!/usr/bin/python3

"""Area of a square"""


class Square:
    """Class Square"""

    def __init__(self, size=0):
        """Intializes Squares

                Args:
                    size (int): size of square

                Returns:
                    None

        """

        self.size = size

    @property
    def size(self, value):
        """Set size of a square

                Args:
                    value (int): size of square

                Retuen:
                    None

                Raises:
                    TypeError: size must be an integer.
                    ValueError: size must be >= 0.

        """

        if type(size) is not int:
            raise TypeError("size must be an integer")
        elif value < 0:
            raise ValueError("size must be >= 0")
        else:
            self.__size = value

    @size.setter
    def area(self):
        """Area of Square

            Args:
                None

            Returns:
                Area of Square

        """

        return (self.__size ** 2)
