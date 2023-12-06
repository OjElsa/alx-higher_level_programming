#!/usr/bin/python3

""" appends a string at the end of a textfile and return characters added"""


def append_write(filename="", text=""):
    """append a string at end of file

        Args:
            filename (str): Path to the file.
            text (str): The string to be appended to the file.

        Returns:
            int:number of characters printed
    """

    with open(filename, "a", encoding="UTF-8") as file:
        file.write(text)
    return len(text)
