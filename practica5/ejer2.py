import math

primes = []
limit = int(input("Introduce un numero: "))

def is_prime(number):
    for i in range(2, int(math.sqrt(number)) + 1):
        if number % i == 0:
            return False
    return True

for i in range(2, limit + 1):
    if is_prime(i):
        primes.append(i)

print(primes)
