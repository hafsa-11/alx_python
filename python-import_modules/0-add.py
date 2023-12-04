#!/usr/bin/python3
# add_0.py file content
# def add(a, b):
#     return a + b

# main program
if _name_ == "_main_":
    a = 1
    b = 2
    from add_0 import add

    result = add(a, b)
    print("{} + {} = {}".format(a, b, result))