N, K = map(int, input().split())

ans = 0
for i in range(1, N+1):
    for j in range(1, N+1):
        for k in range(1, N+1):
            if i + j + k == K:
                ans += 1

print(ans)