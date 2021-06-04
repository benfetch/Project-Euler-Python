def chain_ends(n):
    if n == 1 or n == 89:
        return n

    else:
        x = str(n)
        sum = 0
        for i in x:
            sum += (int(i))**2
            return chain_ends(sum)

count = 0
for i in range(1, 10000000):
    if chain_ends(i) == 89:
        count += 1

print(count)
