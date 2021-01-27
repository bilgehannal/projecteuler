import bios

numbers = bios.read('input.csv')

sum_of_numbers = 0

for i in numbers:
    sum_of_numbers += int(i[0])

print(sum_of_numbers)