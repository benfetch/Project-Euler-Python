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

# n = 1
# while True:
#     x = n * (n+1) // 2
#     if isPentagonal(x) and isHexagonal(x):
#         print(x)
#
#     n += 1
