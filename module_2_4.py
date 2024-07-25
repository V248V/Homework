numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15]
primes = []
not_primes = []
is_prime = 0

for i in numbers:
    for j in range(2, i + 1):
        if i != j and i % j == 0:
            not_primes.append(i)
            break
        elif i != 3 and i % 3 == 0:
            not_primes.append(i)
            break
        else:
            primes.append(i)
            break

print(primes)
print(not_primes)
