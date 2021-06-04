from euclideanAlgoGcm import gcm


#listoffractions = []

# for i in range(2, 100):
#     for j in range(1, i):
#
#         if gcm(i, j) == 1:
#             x = j/i
#             listoffractions.append([x, i, j])
#
#print(sorted(listoffractions))
currentx = (0, 1)
for i in range(2, 1000000):
    j = int(3*i/7)
    print(i, j, currentx)

    if j / i > currentx[0]/currentx[1] and i != 7 and gcm(i, j) == 1:
        currentx = [j, i]

print(currentx[0])
