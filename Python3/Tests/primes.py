import time

def genPrimes():
    primes = [2]
    x = 3
    while True:
        check = True
        t0 = time.time()
        for primnum in primes:
            if x%primnum == 0:
                check = False
        if check:
            primes.append(x)
            yield x
            timer = time.time() - t0
        x += 1
        if timer>1:
            break



for prime in genPrimes():
    print(prime)
