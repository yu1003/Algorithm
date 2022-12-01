n, y = map(int, input().split())

loop_n = n + 1
for i in range(loop_n): # 10000
    for m in range(loop_n - i): # 5000
        o = n - i - m
        if 10000 * i + 5000 * m + 1000 * o == y:
            print(i, m, o)
            exit()
print("-1 -1 -1")