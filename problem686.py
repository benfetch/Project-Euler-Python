def powersOfTwo(L, x):
    n = 1
    xmom = 0
    while True:
        L = str(L)
        length = len(L)
        if len(str(2**n))< length:
            n += 1
        elif str(2**n)[:length] != L:
            n += 1
        else:
            xmom += 1
            if xmom == x:
                return n
            n += 1

print(powersOfTwo(12, 1))
print(powersOfTwo(12, 2))
print(powersOfTwo(123, 45))
print(powersOfTwo(123, 678910))
