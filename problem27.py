import math

def isPrime(n):
    if n==1:
        return False
    elif n<4:
        return True
    elif n % 2 == 0:
        return False
    elif n<9:
        return True
    elif n % 3 == 0:
        return False
    else:
        r = (math.sqrt(n))//1
        f=5
        while f<=r:
            if n % f == 0:
                return False

            elif n % (f+2) == 0:
                return False

            f += 6
    return True


def sum_of_quadratic(x, a, b):
    return (x**2) + a * x + b


b = []
for i in range(2, 1000):
    if isPrime(i):
        b.append(i)

a = list(range(-1000, 1001))
maximum = 0
for i in a:
    for j in b:
        if i+j < 0 or not isPrime(i+j):
            continue
        n = 0
        while True:
            if isPrime(sum_of_quadratic(n, i, j)):
                n += 1
                if n > maximum:
                    maxi = i
                    maxj = j
                    maximum = n
            else:
                break

print(maximum, maxi, maxj)
