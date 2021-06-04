x = 1

while True:
    n1 = str(x)
    n2 = str(x*2)
    n3 = str(x*3)
    n4 = str(x*4)
    n5 = str(x*5)
    n6 = str(x*6)
    x1 = sorted(list(n1))
    x2 = sorted(list(n2))
    x3 = sorted(list(n3))
    x4 = sorted(list(n4))
    x5 = sorted(list(n5))
    x6 = sorted(list(n6))

    if x1 == x2 == x3 == x4 == x5 == x6 :
        print(n1)
        break
    else:
        x += 1
