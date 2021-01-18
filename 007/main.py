def get_prime_numbers(number_of_prime_numbers):
    prime_nubmers = [2, 3, 5]
    test_number = 7
    while len(prime_nubmers) < number_of_prime_numbers:
        for num in prime_nubmers:
            if num <= (test_number ** 0.5):
                if test_number % num == 0:
                    break
            else:
                prime_nubmers.append(test_number)
                break
        test_number += 2
    return prime_nubmers

print(get_prime_numbers(10001)[-1])
                 