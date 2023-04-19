# Task 10: There are n coins on the table. Some of them lie tails up,
# and some have - a coat of arms. Determine the minimum number of coins
# that must be flipped so that all coins are turned on the same side.
# Print the minimum number of coins to flip
print("Task 10: \n")
n = int(input("coins on the table: "))
count_zero = 0
count_one = 0
for i in range(n):
    x = int(input("Smth: "))
    if x == 0:
        count_zero += 1
    else:
        count_one += 1
if count_one > count_zero:
    print(f"number of coins to flip: {count_zero}")
else:
    print(f"number of coins to flip: {count_one}")

# Task 12: Petya and Katya are brother and sister. Petya is a student,
#  and Katya is a schoolgirl. Petya helps Katya with math.
#  He thinks of two natural numbers X and Y (X,Y≤1000), and Katya
#  has to guess them. To do this, Petya makes two clues. He calls
# the sum of these numbers S and their product P. Help Katya guess
#  the numbers conceived by Petya.
print("Task 12: \n")
x = int(input("First hint:the sum of these numbers S: "))
y = int(input("Second hint: their product P: "))
for i in range(x):
    for j in range(y):
        if x == i + j and y == i * j:
            print(f"First number = {i}, Second =  {j}")
            break
    else:
        continue
    break
else:
    print("No solution")

# Task 14: It is required to print all integer powers of two
# (that is, numbers of the form 2k) that do not exceed the number N.
print("Task 14: \n")
n = int(input("Type number N: "))
i = 0
while 2 ** i <= n:
    print(2 ** i)
    i += 1
