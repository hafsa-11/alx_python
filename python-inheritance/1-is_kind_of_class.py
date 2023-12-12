def is_kind_of_class(obj, a_class):
    """
    Check if the object is an instance of, or if it is an instance
    of a class that inherited from the specified class.

    :param obj: The object to check.
    :param a_class: The class or a tuple of classes to check against.
    :return: True if the object is an instance of the specified class, else False.
    """
    return isinstance(obj, a_class)

# Test cases
a = 1
if is_kind_of_class(a, int):
    print("{} comes from {}".format(a, int._name_))
if is_kind_of_class(a, float):
    print("{} comes from {}".format(a, float._name_))
if is_kind_of_class(a, object):
    print("{} comes from {}".format(a, object._name_))