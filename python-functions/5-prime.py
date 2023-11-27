#!/usr/bin/python3

def is_prime(number):
    # Check for numbers less than 2
    if number < 2:
        return False

    # Check for divisibility by numbers from 2 to the square root of the number
    for i in range(2, int(number**0.5) + 1):
        if number % i == 0:
            return False

    # If no divisors are found, the number is prime
    return True