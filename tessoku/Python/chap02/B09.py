##
N = int(input())
A, B, C, D = [None] * N, [None] * N, [None] * N, [None] * N
for t in range(N):
    A[t], B[t], C[t], D[t] = map(int, input().split())

T = [[0] * 1501 for _ in range(1501)]
for t in range(N):
    a, b, c, d = A[t], B[t], C[t], D[t]
    T[b][a] += 1
    T[d][a] -= 1
    T[b][c] -= 1
    T[d][c] += 1

for i in range(0, 1501):
    for j in range(1, 1501):
        T[i][j] += T[i][j-1]
for j in range(0, 1501):
    for i in range(1, 1501):
        T[i][j] += T[i-1][j]

ans = 0
for i in range(1501):
    for j in range(1501):
        if T[i][j] >= 1:
            ans += 1
print(ans)