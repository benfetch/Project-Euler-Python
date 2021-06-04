mat = []
x = open("text.txt")
for i in range(100):
    mat.append(int(x.readline()[:13]))
sum = 0
for i in mat:
    sum += i

sum = str(sum)
print(sum[0:10])
