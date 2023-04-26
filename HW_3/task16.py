# Task 16: It is required to calculate how many times a certain number X occurs in array A.
# In the first line, the user enters a natural number N - the number of elements in the array.
# The following lines contain N integers Ai(you can use pseudo-generation). The last line contains the number X.

# Example:

# 5
# 7 - 2 3 5 1
# 3
# -> 1

from random import randint

amt = input("Input amt: ")
if amt.isdigit():
    amt = int(amt)
    arr = [randint(-9, 9) for i in range(amt)]
    print(arr)
    num = input("Input num: ")
    if num.isdigit():
        num = int(num)
        count = 0
        for numArr in arr:
            if num == numArr:
                count += 1
        print("->", count)
    else:
        print("Uncorrect input")
else:
    print("Uncorrect input")
