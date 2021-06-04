import math

xmin = int(math.sqrt(1020304050607080900)) + 1
xmax = math.sqrt(1929394959697989990)

while xmin < xmax:
    xsquared = xmin ** 2
    xsquared = str(xsquared)
    textx = xsquared[0::2]

    if textx == '1234567890':
        print(xmin)
        break
    else:
        xmin += 1
