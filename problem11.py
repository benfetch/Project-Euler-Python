x = open('text.txt')
mat = []
for i in range(20):
    a = (x.readline().split())
    y = [int(i) for i in a]
    mat.append(y)
print(mat)

# horizontal
maximum = 0
for i in range(20):
    for j in range(17):
        prod = mat[i][j] * mat[i][j+1] * mat[i][j+2] * mat[i][j+3]
        if prod > maximum:
            maximum = prod

# vertical
for i in range(17):
    for j in range(20):
        prod = mat[i][j] * mat[i+1][j] * mat[i+2][j] * mat[i+3][j]
        if prod > maximum:
            maximum = prod

# first diagonal
for i in range(17):
    for j in range(17):
        prod = mat[i][j] * mat[i+1][j+1] * mat[i+2][j+2] * mat[i+3][j+3]
        if prod > maximum:
            maximum = prod

# second diagonal
for i in range(17):
    for j in range(17):
        prod = mat[i][j+3] * mat[i+1][j+2] * mat[i+2][j+1] * mat[i+3][j]
        if prod > maximum:
            maximum = prod

print(maximum)
