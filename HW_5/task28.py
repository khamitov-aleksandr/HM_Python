# Task 28: Write a recursive sum(a, b) function that returns the sum of two non-negative integers.
# Of all the arithmetic operations, only +1 and -1 are allowed. You can't use loops either.

# Example:
# 2 2
# 4

def summ(a, b):
    if b == 0:
        return a
    elif b > 0:
        return summ(a + 1, b - 1)
    else:
        return summ(a - 1, b + 1)


a = int(input("Enter the non-negative integer number: "))
b = int(input("Enter another the non-negative integer number: "))
print("The result of summ is: ", summ(a, b))
