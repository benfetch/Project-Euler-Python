def isPalindrome(n):
    isPal = True
    n = str(n)
    for i in range(len(n)//2):
        if n[i] != n[-i-1]:
            isPal = False
    return isPal


def isLychrel(n):

    for i in range(50):
        r = str(n)[::-1]
        r = int(r)
        x = n + r
        if isPalindrome(x):
            return False
        else:
            n = x

    else:
        return True

count = 0
for i in range(10000):
    if isLychrel(i):
        count += 1

print(count)
