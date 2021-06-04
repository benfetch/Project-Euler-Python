def sum_power_digits(n, x):
    sum = 0
    for i in str(n):
        sum += int(i) ** x

    return sum
listNumbers = []
for i in range(2, 194980):
    if i == sum_power_digits(i, 5):
        listNumbers.append(i)
print(listNumbers)
sum = 0
for i in listNumbers:
    sum += i
print(sum)
