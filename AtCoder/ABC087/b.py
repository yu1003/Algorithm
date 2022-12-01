a, b, c, x = map(int, [input() for i in range(4)])

count = 0
for n in range(a+1):
    for m in range(b+1):
        for l in range(c+1):
            rest = x - (n * 500 + m * 100 + l * 50)
            if rest == 0:
                count += 1
print(count)