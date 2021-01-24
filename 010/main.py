primes = [2, 3]

def find_primes_until(num):
    procces = 5
    while  procces < num:
        for i in primes:
            if i <= procces ** 0.5:
                if procces % i == 0:
                    break
                else:
                    continue
            else:
                primes.append(procces)
                break
        procces += 2
    return primes

primes = find_primes_until(2000000)

print(sum(primes))