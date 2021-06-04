def sum_self_powers(n):
    sum = 0
    for i in range(1, n+1):
        sum += i ** i

    return sum

x = str(sum_self_powers(1000))[-10:]
print(x)
