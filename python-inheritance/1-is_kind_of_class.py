"""
This module provides a function to check if an object is an instance of a specified class or its subclass.
"""

def is_kind_of_class(obj, a_class):
    """
    Check if obj is an instance of, or if obj is an instance of a class that inherited from, a_class.

    :param obj: Object to check
    :param a_class: Class to check against
    :return: True if obj is an instance of a_class or its subclass, otherwise False
    """
    return isinstance(obj, a_class)