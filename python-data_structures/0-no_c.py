def no_c(my_string):
    """Remove all occurrences of 'c' and 'C' from the given string.

    Args:
        my_string (str): The input string.

    Returns:
        str: The new string with 'c' and 'C' removed.
    """
    result = ""
    for char in my_string:
        if char.lower() != 'c':
            result += char
    return result

# Test the function with the provided examples
print(no_c("Holberton School"))
print(no_c("Chicago"))
print(no_c("C is fun!"))