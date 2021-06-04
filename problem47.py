from isPrime import *


def get_prime_factors(n):
    list1 = []
    for i in range(2, n//2+1):
        if n % i == 0 and isPrime(i):
            list1.append(i)
    return list1


i = 1
x = 4
while True:
    print(i)

    if len(get_prime_factors(i)) != x:
        i += 1
        continue
    elif len(get_prime_factors(i+1)) != x:
        i+=1
        continue
    elif len(get_prime_factors(i+2)) != x:
        i+=1
        continue
    elif len(get_prime_factors(i+3)) != x:
        i+=1
        continue
    else:
        print(i)
        break
