# Task 26: Write a program that takes two numbers A and B
# as input and raises the number A to the integer power of B using recursion.

# Example:

# A=3; B = 5 -> 243 (3⁵)
#    A = 2; B = 3 -> 8
import math


def power(base, exp):
    if exp == 0:
        return 1
    if exp < 0:
        return 1 / power(base, -exp)
    if exp % 2 == 0:
        return power(base, exp // 2) * power(base, exp // 2)
    else:
        return power(base, exp - 1) * base


base = int(input("Enter the number: "))
exp = int(input("Enter its exponent: "))
print("The result of exponentiation is: ", power(base, exp))
