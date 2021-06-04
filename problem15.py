from math import factorial

def comb(n, k):
    return (factorial(n))//((factorial(k))* (factorial(n-k)))

print(comb(40,20))
