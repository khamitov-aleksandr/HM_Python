# Problem 18: It is required to find in the array A the element closest in size to a given number X.
# If there are several such elements, you print any one.
# The user in the first line enters a natural number N - the number of elements in the array.
# The following lines contain N integers Ai(you can use pseudo-generation). The last line contains the number X

# Example:
# 5
# 7 - 2 3 5 1
# 6
# -> 7

import random

n = int(input('Enter number of elements in array: '))
list = []
for i in range(n):
    list.append(random.randint(-5, 5))
    list.sort()
print(list)

k = int(input('Enter number X: '))
m = list[0]
for i in range(n):
    if list[i] <= k:
        m = list[i]
    else:
        print(m)
        break
else:
    print(m)
