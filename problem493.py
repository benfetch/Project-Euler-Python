import random

total = 0
for i in range(1000000):
    list1 = 'a' * 10 + 'b' * 10 + 'c' * 10 + 'd' * 10 + 'e' * 10 + 'f' * 10 + 'g' * 10
    list1 = list(list1)
    random.shuffle(list1)
    list_chosen = list1[:20]
    set_list = set(list_chosen)
    x = len(set_list)
    total += x

print(total/1000000)
