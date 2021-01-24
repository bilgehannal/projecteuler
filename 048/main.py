last = 1000
sum_of_numbers = 0

for i in range(1, last+1):
    sum_of_numbers += (i**i)

print(str(sum_of_numbers)[-10:])
