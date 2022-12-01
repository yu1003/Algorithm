N = int(input())

ans = ''
for i in range(9, -1, -1):
    ans += str(N // 2 ** i % 2)

print(ans)