n = 2
listEuler = []
listEuler.append(1504170715041707 % 4503599627370517)
while len(listEuler) < 25:
    x = (1504170715041707 * n) % 4503599627370517
    if x > listEuler[-1]:
        n += 1
    else:
        listEuler.append(x)
        print(listEuler[-1], n)
        n += 1
sum = 0
for i in listEuler:
    sum += i

print(sum)
