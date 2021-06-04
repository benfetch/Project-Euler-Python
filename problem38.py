def concatenate(x, n):
    string = ''
    for i in range(1, n+1):
        string += str(x*i)
    return string

x = 1
while True:
    for n in range(1, 6):
        if sorted(list(concatenate(x, n))) == list('123456789'):
            print(x, n, concatenate(x, n))

    x += 1
