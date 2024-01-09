#!/usr/bin/python3

"""Inserts text after lines in a file."""


def append_after(filename="", search_string="", new_string=""):
    """Inserts text after lines matching a string."""
    text = ""
    with open(filename) as r:
        for line in r:
            text += line
            if search_string in line:
                text += new_string
    with open(filename, "w") as w:
        w.write(text)
