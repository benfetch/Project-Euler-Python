maxno = 0

for i in range(999, 0, -1):
    for j in range(999, 0, -1):
        x = i * j
        single = x % 10
        tens = (x // 10) % 10
        hundreds = (x // 100) % 10
        thousands = (x // 1000) % 10
        ten_thousands = (x // 10000) % 10
        hundred_thousands = (x // 100000) % 10
        if single == hundred_thousands and tens == ten_thousands and hundreds == thousands and x > maxno:
            maxno = x
            break


print(maxno)
