#!/usr/bin/python3


"""a function that reads a text file and prints in stdout"""


def read_file(filename=""):
    """reads a text file

        Args:
            filename (str): Path to the file name
    """
    with open(filename, encoding="UTF-8") as file:
        for line in file:
            print(line, end="")
