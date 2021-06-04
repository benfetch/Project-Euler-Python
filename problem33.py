for j in range(11,100):
    for i in range(11, j):
        if i == j:
            continue
        x = i/j

        a1, a2 = str(i)
        b1, b2 = str(j)

        if a1 != b2 and a2 != b1:
            continue

        elif a1 == b2 and a2 != b1:
            if int(b1) == 0:
                continue
            n = int(a2) / int(b1)
            if n == x:
                print(a2, b1)
        elif a2 == b1 and a1 != b2:
            if int(b2) == 0:
                continue
            n = int(a1) / int(b2)
            if n == x:
                print(a2, b1)
        elif a2 == b1 and a1 == b2:
            if int(b1) == 0 or int(b2) == 0:
                continue
            n1 = int(a1) / int(b2)
            n2 = int(a2) / int(b1)
            if n1 == x or n2 == x:
                print(a , b)
