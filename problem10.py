list_primes = [2]
sum_primes = 2
for i in range(3, 2000000, 2):
    for j in list_primes:
        if i % j == 0:
            break
    else:
        list_primes.append(i)
        
        sum_primes += i

print(sum_primes)
