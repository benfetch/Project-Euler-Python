import math


def sum_digit_factorials(n):
    sum = 0
    for i in str(n):
        sum += math.factorial(int(i))
    return sum


def chain_of_factorials(n):
    count = 1
    x = n
    list_chain = [x]
    while True:

        n = sum_digit_factorials(n)
        if n in list_chain:
            return count

        else:
            list_chain.append(n)
            count += 1


count = 0
for i in range(2, 1000000):
    if chain_of_factorials(i) == 60:
        count += 1

print(count)
