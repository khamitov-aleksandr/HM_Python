print("Task 2")
# Task 2: Find the sum of the digits of a three-digit number.
# *Example:*
# 123 -> 6 (1 + 2 + 3)
# 100 -> 1 (1 + 0 + 0) |
three_digit_number = int(input("Enter a three-digit number :"))
if (three_digit_number > 999) or (three_digit_number < 100):
    print("Sorry, you enter NOT a three-digit number, start again")
else:
    first = int(three_digit_number / 100)
    second = int((three_digit_number % 100) / 10)
    third = three_digit_number % 10
    print(first + second + third)
print("Task 4")
# Petya, Katya and Seryozha make paper cranes.
# Together they made S cranes. How many cranes did each child make if it is known that Petya and Seryozha
# made the same number of cranes, and Katya made twice as many cranes as Petya and Seryozha together?
# *Example:*
# 6 -> 1 4 1
# 24 -> 4 16 4
# 60 -> 10 40 10
all_toghether = int(input("How many paper cranes was made? "))
if not (all_toghether % 6 == 0):
    print("Sorry, you enter wrong number of paper cranes")
else:
    petya_or_seryozha = int(all_toghether / 6)
    katya = petya_or_seryozha * 4
    print(petya_or_seryozha, katya, petya_or_seryozha)
print("Task 6")
# Do you use public transport?
# You probably paid for the fare and received a ticket with a number.
# A lucky ticket is a ticket with a six-digit number,
# where the sum of the first three digits is equal to the sum of the last three.
# Those. ticket number 385916 is lucky, because 3+8+5=9+1+6.
# You need to write a program that checks if a ticket is lucky.
# *Example:*
# 385916 -> yes
# 123456 -> no
ticket_number = input("Enter your number of ticket: ")
if (len(ticket_number) < 6) or (len(ticket_number) > 6):
    print("Sorry, you enter NOT a six digit number, start again")
else:
    ticket_number = int(ticket_number)
    first_digit = int(ticket_number / 100000)
    second_digit = int((ticket_number / 10000) % 10)
    third_digit = int((ticket_number / 1000) % 10)
    fourth_digit = int((ticket_number / 100) % 10)
    fifth_digit = int((ticket_number / 10) % 10)
    sixth_digit = int(ticket_number % 10)
    sum_one = first_digit + second_digit + third_digit
    sum_two = fourth_digit + fifth_digit + sixth_digit
    if sum_one == sum_two:
        print("yes")
    else:
        print("no")
print('\n')
print("Task 8")
# It is required to determine whether it is possible to break off k slices from a chocolate bar of size n × m
# if it is possible to make one break in a straight line between the slices
# (that is, to break the chocolate bar into two rectangles).
# *Example:*
# 3 2 4 -> yes
# 3 2 1 -> no
n = int(input("Enter a first side(sixe n): "))
m = int(input("Enter a second side(sixe m): "))
k = int(input("Enter a number of slices(k slices): "))
if k in range(n, m*n, n) or k in range(m, m*n, m):
    print("yes")
else:
    print("no")
