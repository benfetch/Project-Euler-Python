from euclideanAlgoGcm import gcm


def phi(n):
    res = 1
    for i in range(2, n):
        if gcm(n, i) == 1:
            res += 1
    return res


print(phi(510510))

# maximum = 0
# maxval = 0
# for i in range(1000001):
#     if i/phi(i) > maximum:
#         maxval = i
#         maximum = i/phi(i)
#
# print(maximum, maxval)
