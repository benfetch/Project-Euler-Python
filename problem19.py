month_start = []
first_day = 0
for year in range(1901, 2001):
    for month in range(12):
        month_start.append(first_day)
        if month == 1 and year % 4 == 0 and year % 400 == 0:
            first_day += 29
            first_day %= 7
        elif month == 1 and year % 4 == 0 and year % 400 != 0:
            first_day += 28
            first_day %= 7
        elif month == 1 and year % 4 != 0:
            first_day += 28
            first_day %= 7
        elif month in [3, 5, 8, 10]:
            first_day += 30
            first_day %= 7
        else:
            first_day += 31
            first_day %= 7

print(month_start)

print(month_start.count(6))
month == 1 and year % 4 == 0 and year % 400 == 0:
