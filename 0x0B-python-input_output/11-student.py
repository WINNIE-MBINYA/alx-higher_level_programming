#!/usr/bin/python3


"""Defines a Student class."""


class Student:
    """Models a student."""

    def __init__(self, first, last, age):
        """Creates a new Student."""
        self.first_name = first
        self.last_name = last
        self.age = age

    def to_json(self, attrs=None):
        """Returns JSON representation."""
        # ... (docstring for conditional logic omitted for brevity)

    def reload_from_json(self, json):
        """Replaces attributes from JSON."""
        for k, v in json.items():
            setattr(self, k, v)
