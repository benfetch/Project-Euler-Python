def numberOfRightTriangles(p):
    count = 0
    for o in range(1, int(p//2)):
        num = p**2 - 2*p*o
        den = 2*p-2*o
        a = num//den
        if a < o:
            break
        if (num%den==0):
            count+=1  
    return count

max_value = 0
max_count = 0
for p in range(3,1001):
    n = numberOfRightTriangles(p)
    if n>max_count:
        max_count = numberOfRightTriangles(p)
        max_value = p
print(max_count, max_value)