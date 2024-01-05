#!/usr/bin/python3
class LockedClass():
    """A class that prevents the dynamic creation of new instance attributes"""
    __slots__ = ['first_name']

    def __init__(self):
        """Initializes an instance of LockedClass"""
        pass
