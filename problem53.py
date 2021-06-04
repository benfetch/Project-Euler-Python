

def choose(n, k):
    if k == 0:
        return 1
    a = 1
    b = 1
    for i in range(k):
        a *= n - i
        b *= (1+i)
        print(a, b)

    return a // b

count = 0
for n in range(1, 101):
    if n % 2 != 0:
        for r in range(1, n//2+1):
            if choose(n, r) > 1000000:
                count += 2
    else:
        for r in range(1, n//2):
            if choose(n, r) > 1000000:
                count += 2
        if choose(n, n//2) > 1000000:
            count += 1


print(count)
