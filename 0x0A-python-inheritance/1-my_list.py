#!/usr/bin/python3

"""a class MyList that inherits from list"""


class MyList(list):
    """A class custom list"""
    def print_sorted(self):
        """Prints the sorted list in ascending order"""
        print(sorted(self))
