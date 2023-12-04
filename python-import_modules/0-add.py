#!/usr/bin/python3
a = 1
b = 2

if _name_ == "_main_":
    add_0 = _import_('add_0')
    print("{} + {} = {}".format(a, b, add_0.add(a, b)))