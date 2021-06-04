def sum_of_first_n_squares(n):
    sum1 = 0
    for i in range(1, n + 1):
        sum1 += i ** 2
    return sum1

def sum_of_first_n_iter(n):
    sum1 = 0

    for i in range(1, n+1):
        sum1 += i
    return sum1



def sum_of_first_n(n):
    return n * (n + 1) // 2

n = 100

x = sum_of_first_n_iter(n)
y = sum_of_first_n(n)

print(x, y)
