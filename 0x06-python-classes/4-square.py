#!/usr/bin/python3

class Square:
    def __init__(self, size=0):
        """
        Initialization of new square
        args:
            size (int): size of square
        
        """
        self.size = size

    @property
    def size(self): #set current size of square
        return (self.__size)

    @size.setter
    def size(self, value):
        if not isinstance(value, int):
            raise TypeError("size must be an integer")
        elif value < 0:
            raise ValueError("size must be >= 0")
        self.__size = value

    def area(self): #Returns current square area
        return (self.__size * self.__size)
