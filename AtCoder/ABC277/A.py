N, X = map(int, input().split())
P = list(map(int, input().split()))

ans = 0
for n in range(1, N+1):
    if P[n-1] == X:
        ans = n
        break

print(ans)