import bios

NUMBER_OF_ADJ_NUMBER = 4
data = bios.read('input.csv')
number_of_row = len(data)
number_of_column = len(data[0])

max_product_of_try = 0

for i in range(number_of_row - NUMBER_OF_ADJ_NUMBER + 1):
    for j in range(number_of_column - NUMBER_OF_ADJ_NUMBER + 1):
        product_of_try = int(data[i][j]) * int(data[i+1][j+1]) * int(data[i+2][j+2]) * int(data[i+3][j+3])
        if product_of_try > max_product_of_try:
            max_product_of_try = product_of_try

for i in range(number_of_row - NUMBER_OF_ADJ_NUMBER + 1):
    for j in range(number_of_column - NUMBER_OF_ADJ_NUMBER + 1):
        product_of_try = int(data[i+3][j]) * int(data[i+2][j+1]) * int(data[i+1][j+2]) * int(data[i][j+3])
        if product_of_try > max_product_of_try:
            max_product_of_try = product_of_try

for i in range(number_of_row - NUMBER_OF_ADJ_NUMBER + 1):
    for j in range(number_of_column):
        product_of_try = int(data[i][j]) * int(data[i+1][j]) * int(data[i+2][j]) * int(data[i+3][j])
        if product_of_try > max_product_of_try:
            max_product_of_try = product_of_try

for i in range(number_of_row):
    for j in range(number_of_column - NUMBER_OF_ADJ_NUMBER + 1):
        product_of_try = int(data[i][j]) * int(data[i][j+1])* int(data[i][j+2]) *int( data[i][j+3])
        if product_of_try > max_product_of_try:
            max_product_of_try = product_of_try

print(max_product_of_try)


