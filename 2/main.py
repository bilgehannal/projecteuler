fib_numbers = [1, 2]
index = 1

sum_of_evens = 0

while True:
    new_number = fib_numbers[index] + fib_numbers[index - 1]
    if new_number > 4000000:
        break
    fib_numbers.append(new_number)
    index += 1

for fib_number in fib_numbers:
    if fib_number % 2 == 0:
        sum_of_evens += fib_number

print(sum_of_evens)
