# Task 26: Write a program that takes two numbers A and B
# as input and raises the number A to the integer power of B using recursion.

# Example:

# A=3; B = 5 -> 243 (3⁵)
#    A = 2; B = 3 -> 8


def power(base, exp):
    if (exp == 1):
        return (base)
    if (exp != 1):
        return (base * power(base, exp - 1))


base = int(input("Enter the number: "))
exp = int(input("Enter its exponent: "))
print("The result of exponentiation is: ", power(base, exp))
