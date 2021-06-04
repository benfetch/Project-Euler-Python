x = '0.1'

n = 2
while len(x) < 1000004:
    x += str(n)
    n += 1


print(x)
print(int(x[2]) * int(x[11]) * int(x[101]) * int(x[1001]) * int(x[10001]) * int(x[100001]) * int(x[1000001]))
