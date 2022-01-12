primes = set(range(2,5001))
p = 2

while p <= 5000:
    while p not in primes and p < 5000:
        p += 1
    k = p + p
    while k <= 5000:
        if k in primes:
            primes.remove(k)
        k = k + p
    p += 1

print(primes)