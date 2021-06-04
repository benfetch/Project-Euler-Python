list_items = []

for a in range(2, 101):
    for b in range(2, 101):
        if a**b not in list_items:
            list_items.append(a**b)

print(len(list_items))
