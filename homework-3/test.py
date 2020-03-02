

def getInverse(x, n):
    i = 0
    while True:
        i += 1
        if (x * i) % n == 1:
            return i
        elif i > 300000:
            return -1

n = 55
numbers = range(1, n)

for x in numbers:
    if x % 5 == 0 or x % 11 == 0:
        continue

    actualX = x**3 % n
    inverse = getInverse(actualX, n)
    print(f"{actualX} {inverse}")

print('done')