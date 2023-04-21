# Task 20: * In the board game Scrabble, each letter has a certain value.
# In the case of the English alphabet, points are distributed as follows: A, E, I, O, U, L, N, S, T, R - 1 point
# D, G - 2 points
# B, C, M, P - 3 points
# F, H, V, W, Y - 4 points
# K - 5 points
# J, X - 8 points
# Q, Z - 10 points. And Russian letters are evaluated as follows: А, В, Е, И, Н, О, Р, С, Т - 1 point
# Д, К, Л, М, П, У - 2 points
# Б, Г, Ё, Ь, Я - 3 points
# Й, Ы  - 4 points
# Ж, З, Х, Ц, Ч - 5 points
# Ш, Э, Ю - 8 points
# Ф, Щ, Ъ - 10 points. Write a program that calculates the cost of a word entered by the user. We will assume that only one word is given as input, which contains either only English or only Russian letters.

# *Example: *

# ноутбук
# 12

def scrabble():
    weight = {0: ' ', 1: 'AEIOULNSTRАВЕИНОРСТ', 2: 'DGДКЛМПУ',
              3: 'BCMPБГЁЬЯ', 4: 'FHVWYЙЫ', 5: 'KЖЗХЦЧ', 8: 'JXШЭЮ', 10: 'QZФЩЪ'}
    S = input('Enter a word or phrase in any language to calculate its value: ')
    s = S.upper()
    cost = 0
    val = list()
    for el in s:
        for k, v in weight.items():
            if el in v:
                cost += k
                val.append(str(k))
    sum = ' + '.join(val)
    print(f'the cost is "{S}": {sum}  = {cost}')


scrabble()
