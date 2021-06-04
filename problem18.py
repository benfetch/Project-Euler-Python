def max_path(triangle_list):
    x = len(triangle_list)
    for i in range(x-2, -1, -1):
        for j in range(len(triangle_list[i])):
            print(i, j, triangle_list[i][j])
            a = triangle_list[i+1][j]
            b = triangle_list[i+1][j+1]
            if b > a:
                triangle_list[i][j] += b
            else:
                triangle_list[i][j] += a

    return(triangle_list[0][0])


x = open("problem18.txt").read()
x = x.split("\n")
for i in range(len(x)):
    x[i] = [int(j) for j in x[i].split()]

del x[-1]

print(max_path(x))


def max_path_recursive(triangle_list, index=0):
    print(triangle_list[0][0], index)

    if len(triangle_list) == 1:
        return triangle_list[0][index]
    else:
        a = max_path_recursive(triangle_list[1:], index)
        b = max_path_recursive(triangle_list[1:], index + 1)
        if a > b:
            return triangle_list[0][index] + a
        else:
            return triangle_list[0][index] + b

print(max_path_recursive(x))
