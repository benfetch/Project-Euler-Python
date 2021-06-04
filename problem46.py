from isPrime import isPrime as ip
import math

n = 9
while True:
    print(n)


    if ip(n):
        n += 2
        continue
    for i in range(1, int(math.sqrt(n/2)) + 1):
        print(n, i , (n - 2 * (i**2)))
        if ip(n - 2 * (i**2)):
            n += 2
            break
    else:
        print(n)
        break
