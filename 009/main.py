import math

for a in range(1, 333):
    for b in range(a+1, int(math.floor((1000-a)/2))):
        c = 1000 - a - b
        if (a**2)+(b**2) == (c**2):
            print('a:{} b:{} c: {}, product: {}'.format(a, b, c, a*b*c))