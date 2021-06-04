def score_word(word):
    x = list('ABCDEFGHIJKLMNOPQRSTUVWXYZ')
    y = list(range(1, 27))
    dict_score = dict(zip(x,y))
    score = 0
    for i in word:
        score += dict_score[i]
    return score


file = open('words.txt')
x = file.read()
x = x.strip()
x = x[1:-1]
x = x.split('","')

maximum = 0
for i in x:
    if score_word(i) > maximum:
        maximum = score_word(i)

list_triangle = []
n = 1
while n*(n+1)//2 <= maximum:
    list_triangle.append(n*(n+1)//2)
    n += 1


count = 0
for word in x:
    if score_word(word) in list_triangle:
        count += 1
print(count)
    
