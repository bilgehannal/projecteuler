def get_sum_of_squares_of_first(number):
    s = 0
    for i in range(number):
        s += i ** 2
    return s

def get_square_of_the_sum(number):
    return sum(list(range(number))) ** 2

print(get_square_of_the_sum(101) - get_sum_of_squares_of_first(101))