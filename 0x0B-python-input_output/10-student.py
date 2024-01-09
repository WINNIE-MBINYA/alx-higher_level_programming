#!/usr/bin/python3

"""This module encapsulates the Student class"""


class Student:
    """
    Encapsulates the core properties and methods associated with a student.
    """

    def __init__(self, first_name, last_name, age):
        """
        Constructs a new Student instance with the provided information.

        Args:
            first_name (str): The student's first name.
            last_name (str): The student's last name.
            age (int): The student's age.
        """
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self, attrs=None):
        """
        Generates a dictionary representation of the Student instance.

        Args:
            attrs (list, optional): A list of attribute names to be included.

        Returns:
            dict: Contains the selected attributes and their values.
        """
        if isinstance(attrs, list) and
        all(isinstance(ele, str) for ele in attrs):
            return {k: getattr(self, k) for k in attrs if hasattr(self, k)}
        return self.__dict__
