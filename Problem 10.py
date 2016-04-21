primes = [2, 3, 5, 7, 11, 13]
num = 15
while primes[-1] < 2000000:
    real = True
    for prime in primes:
        if prime > num**0.5:
            break
        if num % prime == 0:
            real = False
            break
    if real == True:
        primes.append(num)
    num += 2
print(sum(primes[:-1]))
