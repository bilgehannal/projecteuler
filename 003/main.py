def get_prime_numbers_until(max_number):
    prime_nubmers = [2, 3, 5]
    test_number = 7
    while test_number <= max_number:
        for num in prime_nubmers:
            if num < (test_number ** 0.5):
                if test_number % num == 0:
                    break
            else:
                prime_nubmers.append(test_number)
                break
        test_number += 2
    return prime_nubmers

spesific_number = 600851475143
prime_factors_of_spesific_nubmer = []

for prime_number in get_prime_numbers_until(spesific_number ** 0.5):
    if spesific_number % prime_number == 0:
        prime_factors_of_spesific_nubmer.append(prime_number)

print(prime_factors_of_spesific_nubmer[-1])
                 