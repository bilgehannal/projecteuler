import math

def get_number(n):
    return int(n * (n+1) / 2)

def get_num_of_divisors(n):
    counter = 0
    for i in range(1, int(math.sqrt(n))+1):
        if n % i == 0:
            if(n/1 == i):
                counter += 1
            else:
                counter += 2
    return counter

maximum = 0

i = 1
while True:
    number = get_number(i)
    num_of_divisors = get_num_of_divisors(number)
    if num_of_divisors > maximum:
        maximum = num_of_divisors
        print(maximum)
    if num_of_divisors >= 500:
        print('Number: {}, divisors: {}'.format(number, num_of_divisors))
        break
    i += 1
