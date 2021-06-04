import math


def no_factors(n):
    count = 0
    i = 1
    while i <= math.sqrt(n):
        if n % i == 0:
            if n // i == i:
                count += 1
            else:
                count += 2
        i += 1

    return count



n = 1
while True:
    sum1 = n * (n+1) // 2
    x = no_factors(sum1)
    if x > 500:
        print(n, sum1, x)
        break
    n += 1
