def get_score(name):
    letterScore = {}
    alphabet = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    for i in range(26):
        letterScore[alphabet[i]] = i + 1

    score = 0
    for i in name:
        score += letterScore[i]
    return score


myNames = open("names.txt").read()[1:-1]
myNames = myNames.split('","')
myNames.sort()
score = 0
for i in range(len(myNames)):
    score += get_score(myNames[i]) * (i + 1)

print(score)
