from isPrime import isPrime
list_primes = []
for i in range(2, 1000000):
    if isPrime(i):
        list_primes.append(i)
b = 0

for i in list_primes:
    x = str(i)
    for j in range(len(x)-1):
        a = x[j+1:] + x[:j+1]
        print("these are x", x)

        if not isPrime(int(a)):
            break
    else:
        b += 1
        print(i)

print(b)
