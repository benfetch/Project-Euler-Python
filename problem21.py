def sum_of_divisors(n):

    sum = 0
    for i in range(1, n//2+1):
        if n % i == 0:
            sum += i

    return sum

list1 = []

for i in range(1, 10001):
    j = sum_of_divisors(i)
    if sum_of_divisors(j) == i and i != j and j <=10000:
        list1.append(i)
sum = 0
for i in list1:
    sum += i
print(sum)
