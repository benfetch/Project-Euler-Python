def isPal(n):
    n = str(n)
    for i in range(len(n)//2):
        if n[i] != n[-1-i]:
            return False

    else:
        return True

def isPalBin(n):
    n = str(n)[2:]
    for i in range(len(n)//2):
        if n[i] != n[-1-i]:
            return False

    else:
        return True


sum = 0
for i in range(1000000):
    if isPal(i) and isPalBin(bin(i)):
        sum += i
print(sum)
