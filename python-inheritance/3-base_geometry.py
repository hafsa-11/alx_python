"""
This module provides a base geometry class.
"""


class BaseGeometry:
   def __dir__(self):
        return []

bg = BaseGeometry()

print(bg)
print(dir(bg))
print(dir(BaseGeometry))