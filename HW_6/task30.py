# Task 30: Fill an array with elements of an arithmetic progression.
# Its first element, difference and number of elements must be entered from the keyboard.
# The formula for getting the nth member of the progression is: an = a1 + (n-1) * d.
# Each number is entered on a new line.

a1 = int(input("Enter : "))
d = int(input("Enter : "))
n = int(input("Enter : "))
for i in range(n):
    print(a1 + i * d)
