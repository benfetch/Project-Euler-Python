def is_abundant(n):
    sum = 0
    for i in range(1, n//2):
        if n % i == 0:
            sum += i
    if sum > n:
        return True
list_abundant_nos = []
for i in range(12, 28124):
    if is_abundant(i):
        list_abundant_nos.append(i)
two_abundant_nos = []
for i in list_abundant_nos:
    for j in list_abundant_nos:
        two_abundant_nos.append(i+j)

not_two_abundant = []
for i in range(28124):
    if i not in two_abundant_nos:
        not_two_abundant.append(i)
sum = 0
for i in not_two_abundant:
    sum += i
print(sum)
