def is_number_available(number, multiples):
    for multiple in multiples:
        if number % multiple == 0:
            return True
    return False

maximum_number = 1000
sum_of_numbers = 0
multiples = [3, 5]

for i in range(maximum_number):
    if is_number_available(i, multiples):
        sum_of_numbers += i

print(sum_of_numbers)