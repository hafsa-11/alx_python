def inherits_from(obj, a_class):
    """
    Check if the object is an instance of a class that inherited
    (directly or indirectly) from the specified class.

    :param obj: The object to check.
    :param a_class: The class to check against.
    :return: True if the object inherits from the specified class, else False.
    """
    return issubclass(type(obj), a_class)

# Test cases
a = True
if inherits_from(a, int):
    print("{} inherited from class {}".format(a, int._name_))
if inherits_from(a, bool):
    print("{} inherited from class {}".format(a, bool._name_))
if inherits_from(a, object):
    print("{} inherited from class {}".format(a, object._name_))