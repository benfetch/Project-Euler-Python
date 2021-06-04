import math

n = 600851475143
while n % 2 == 0:
    n //= 2

for i in range(3, int(math.sqrt(n)) + 2, 2):
    while n % i == 0:
        n //= i
        if n == 1:
            n = i
            break


print(n)
