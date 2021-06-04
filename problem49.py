from isPrime import isPrime

list_primes = []

for i in range(1000, 10000):
    if isPrime(i):
        list_primes.append(i)

for i in range(len(list_primes)):
    for j in list_primes[i+1:]:
        k = 2*j - list_primes[i]

        if k not in list_primes:
            continue

        else:
            x, y, z = str(list_primes[i]), str(j), str(k)
            for text in x:
                first_index_y = y.find(text)
                y = y[:first_index_y] + y[first_index_y+1:]
                first_index_z = z.find(text)
                z = z[:first_index_z] + z[first_index_z+1:]

                if len(y) == 0 and len(z) == 0:
                    print(list_primes[i], j, k)
