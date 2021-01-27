from math import comb

number_of_square = 20

total = 0

for i in range(number_of_square + 1):
    total += comb(number_of_square, i)**2

print(total)