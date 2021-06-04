for i in range(1, 10000):
    if (1000*i - 500000)%(i -1000) == 0:
        a = i
        break

b = (1000*i - 500000) // (i -1000)
c = 1000 - a - b

print(a, b, c, a*b*c)
