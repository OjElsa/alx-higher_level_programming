#!/usr/bin/python3

"""writes a string to a text file and returns number of characters written"""


def write_file(filename="", text=""):
    """wrrite a string to a text file

        Args:
            filename (str): Path to the file.
            text (str): The string to be written to the file.

        Return:
            int: number of characters printed
    """

    with open(filename, "w", encoding="UTF-8") as file:
        file.write(text)
    return len(text)
