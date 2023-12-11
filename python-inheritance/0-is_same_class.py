#!/usr/bin/python3
"""
Module: 0-is_same_class

This module defines the is_same_class function.
"""

def is_same_class(obj, a_class):
    """
    Check if obj is exactly an instance of a_class.

    Parameters:
    - obj: The object to check.
    - a_class: The specified class to compare.

    Returns:
    - bool: True if obj is exactly an instance of a_class, otherwise False.
    """

    return type(obj) is a_class

a = 1
if is_same_class(a, int):
    print("{} is an instance of the class {}".format(a, int._name_))
if is_same_class(a, float):
    print("{} is an instance of the class {}".format(a, float._name_))
if is_same_class(a, object):
    print("{} is an instance of the class {}".format(a, object._name_))