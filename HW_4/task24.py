# A farm in Karelia grows blueberries.
# It grows on a round bed, and the bushes are planted only around the circumference.
# Thus, each bush has exactly two neighbors. In total, N bushes grow in the garden.
# These bushes have different yields, so by the time they are harvested,
# they have grown a different number of berries — ai berries have grown on the i-th bush.
# This farm has introduced an automatic blueberry picking system.
# This system consists of a control module and several collecting modules.
# The picking module in one run, being directly in front of a certain bush,
# collects berries from this bush and from two neighboring ones.
# Write a program to find the maximum number of berries that the
# picking module can collect in one run, being in front of some
# bush of the garden bed specified in the input file.

n = int(input())
arr = list()
for i in range(n):
    x = int(input())
    arr.append(x)

arr_count = list()
for i in range(len(arr) - 1):
    arr_count.append(arr[i-1] + arr[i] + arr[i + 1])
arr_count.append(arr[-2] + arr[-1] + arr[0])
print(max(arr_count))
