import math

def sum_of_factorial_digits_equal(n):
    sum = 0
    for i in str(n):
        sum += math.factorial(int(i))
    if sum == n:
        return True
    else:
        return False
list1 = []
for i in range(1000000):
    if sum_of_factorial_digits_equal(i):
        list1.append(i)
print(list1)
