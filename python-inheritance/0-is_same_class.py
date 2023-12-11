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