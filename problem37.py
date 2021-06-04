from isPrime import isPrime


print(isPrime(1))
n = 11
while True:

    x = str(n)
    for i in range(len(x)):
        a, b = x[i:], x[:len(x)-i]
        a, b = int(a), int(b)

        if not (isPrime(a) and isPrime(b)):

            n+=2
            break
    else:
        print(n)
        n += 2
