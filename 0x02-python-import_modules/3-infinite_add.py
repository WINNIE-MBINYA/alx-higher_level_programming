#!/usr/bin/python3
from sys import argv

if __name__ == "__main__":
    # Extracting numerical arguments and summing them
    result = sum(int(arg) for arg in argv[1:])

    # Printing the result
    print(result)
