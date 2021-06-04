a1 = 1
a2 = 1
a3 = a1 + a2
counter = 2

while len(str(a3)) < 1000:
    a3 = a1 + a2
    a1 = a2
    a2 = a3
    counter += 1

print(counter)
