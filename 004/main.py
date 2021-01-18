def is_palindorme(s):
    if s == s[::-1]:
        return True
    return False

max_palindorme = 0

for i in range(100, 1000):
    for j in range(100, 1000):
        if is_palindorme(str(i * j)) and max_palindorme < i * j:
            max_palindorme = i * j
            print("i: {}, j: {}, max: {}".format(i, j, i*j))

print()      
print(max_palindorme)