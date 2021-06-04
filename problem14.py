def count_seq(n, count=1):
    x = count + 1
    if n == 1:
        return count
    elif n % 2 == 0:
        return count_seq(n // 2, x)
    else:
        return count_seq(3*n + 1, x)

#
maximum = 0
for i in range(1, 1000000, 2):


    x = count_seq(i)
    if x > maximum:
        maximum = x
        maxi = i
print(maxi)

#
#
# print(count_seq(20000))
