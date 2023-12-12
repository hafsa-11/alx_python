"""
This module provides a function to check if an object is an instance of a class that inherited (directly or indirectly) from the specified class.
"""

def inherits_from(obj, a_class):
    """
    Check if obj is an instance of a class that inherited (directly or indirectly) from a_class.

    :param obj: Object to check
    :param a_class: Class to check against
    :return: True if obj is an instance of a class that inherited from a_class, otherwise False
    """
    return type(obj) is not a_class and issubclass(type(obj), a_class)