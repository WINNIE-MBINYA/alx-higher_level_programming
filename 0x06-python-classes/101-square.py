#!/usr/bin/python3
"""Print square instance"""


class Square:
    """Represents an instance, square."""

    def __init__(self, size=0, position=(0, 0)):
        """Initializes a new square.

        Args:
            size (int): The size of the new square.
            position (int, int): The position of the new square.
        """
        self.size = size
        self.position = position

    @property
    def size(self):
        """Get or set the current size of the square."""
        return self.__size

    @size.setter
    def size(self, value):
        """Set the size of the square with proper validation."""
        if not isinstance(value, int):
            raise TypeError("Size must be an integer.")
        elif value < 0:
            raise ValueError("Size must be >= 0")
        self.__size = value

    @property
    def position(self):
        """Get or set the current position of the square."""
        return self.__position

    @position.setter
    def position(self, value):
        """Set the position of the square with proper validation."""
        if (not isinstance(value, tuple) or
                len(value) != 2 or
                not all(isinstance(num, int) for num in value) or
                not all(num >= 0 for num in value)):
            raise TypeError("Position must be a tuple of 2 positive integers.")
        self.__position = value

    def area(self):
        """Calculate and return the current area of the square."""
        return self.__size * self.__size

    def my_print(self):
        """Print the square using the '#' character."""
        if self.__size == 0:
            print("")
            return

        [print("") for _ in range(0, self.__position[1])]
        for _ in range(0, self.__size):
            [print(" ", end="") for _ in range(0, self.__position[0])]
            [print("#", end="") for _ in range(0, self.__size)]
            print("")

    def __str__(self):
        """Define the print() representation of a Square."""
        if self.__size != 0:
            [print("") for _ in range(0, self.__position[1])]
        for _ in range(0, self.__size):
            [print(" ", end="") for _ in range(0, self.__position[0])]
            [print("#", end="") for _ in range(0, self.__size)]
            if _ != self.__size - 1:
                print("")
        return ("")
