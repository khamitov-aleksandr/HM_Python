# Task 30: Fill an array with elements of an arithmetic progression.
# Its first element, difference and number of elements must be entered from the keyboard.
# The formula for getting the nth member of the progression is: an = a1 + (n-1) * d.
# Each number is entered on a new line.

a1 = int(input("Enter first element: "))
d = int(input("Enter difference: "))
n = int(input("Enter number of elements: "))
for i in range(n):
    print(a1 + i * d)
