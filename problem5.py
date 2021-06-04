k = 2 * 3 * 5 * 7 * 11 * 13 * 17 * 19
n = 20

while True:
    print(k)
    found = True
    k += 19
    for i in range(3, n + 1):
        if k % i != 0:
            found = False
            break
    if found == True:
        break



print(k)
