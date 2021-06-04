import math

def isSquare(n):
    x = int(math.sqrt(n))
    if x**2 == n:
        return True
    else:
        return False


def isHexagonal(n):
    if not isSquare(1 + 8 * n):
        return False
    elif (1 + int(math.sqrt(1+8*n))) % 4 != 0:
        return False
    else:
        return True


def isPentagonal(n):
    if not isSquare(1 + 24 * n):
        return False
    elif (1 + int(math.sqrt(1+24*n))) % 6 != 0:
        return False
    else:
        return True


for i in range(1, 10000):
    for j in range(i+1, 10000):
        x = i * (3*i - 1) // 2
        y = j * (3*j - 1) // 2
        if isPentagonal(y-x) and isPentagonal(x+y):
            print(x, y, x-y)
