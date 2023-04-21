# Task 22: Given two unordered sets of integers (maybe with repetitions).
# Print without repetition in ascending order all those numbers that occur in both sets.
# The user enters 2 numbers. n is the number of elements of the first set.
# m is the number of elements of the second set.
# The user then enters the elements of the sets themselves.

mol = [int(x) for x in input().split()]
n = mol[0]
m = mol[1]
set_1 = set()
set_2 = set()
list_1 = list()
a = [int(x) for x in input().split()]
k = set(a)
for i in k:
    set_1.add(i)
b = [int(x) for x in input().split()]
k1 = set(b)
for i in k1:
    set_2.add(i)
lok = set_1 & set_2
kool = list(lok)
kool.sort()
for i in kool:
    print(i, end=' ')
