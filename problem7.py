list_of_primes = [2]
k = 3
while len(list_of_primes) < 10001:
    for i in list_of_primes:
        if k % i == 0:
            break
    else:
        list_of_primes.append(k)

    k += 2

print(list_of_primes[-1])
