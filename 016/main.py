power = 1000

number = 2**power
total = 0

str_number = list(str(number))
numbers = [ int(x) for x in str_number ]

print(sum(numbers))
