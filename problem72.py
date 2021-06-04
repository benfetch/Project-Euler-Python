
def gcm(a,b):
    if b > a:
        (a, b) = (b, a)

    if a % b == 0:
        return b
    else:
        return gcm(b, a % b)


count = 0
for b in range(2, 10001):
    for a in range(1, b):
        if gcm(a, b) == 1:
            count += 1

print(count)
