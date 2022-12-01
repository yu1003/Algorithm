N = list(map(int, list(input())))

ans = 0
for i in range(len(N)):
    ans += N[-(i+1)] * 2 ** i

print(ans)