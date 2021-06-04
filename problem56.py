def digital_sum(n):
    sum = 0
    for i in str(n):
        sum += int(i)
    return sum

maximum = 0
for a in range(1, 101):
    for b in range(1, 101):
        x = a**b
        print(x)
        if digital_sum(x) > maximum:
            maximum = digital_sum(x)

print(maximum)
