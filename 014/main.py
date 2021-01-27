def get_next(n):
    if n % 2 == 0:
        return int(n/2)
    else:
        return int(3*n + 1)

def get_sequence(starting_number):
    sequence = [starting_number]
    while sequence[-1] != 1:
        sequence.append(get_next(sequence[-1]))
    return sequence

maximum = 0
maximum_number = 0

for i in range(2, 1000001):
    sequence = get_sequence(i)
    number_of_element = len(sequence)
    print('number: {}, n_of_element: {}'.format(i, number_of_element))
    if number_of_element > maximum:
        maximum = number_of_element
        maximum_number = i

print('maximum Number: {}, maximum element: {}'.format(maximum_number, maximum))
