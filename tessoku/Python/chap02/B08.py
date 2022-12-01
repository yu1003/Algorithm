N = int(input())
X, Y = [None] * N, [None] * N
for n in range(N):
    X[n], Y[n] = map(int, input().split())
Q = int(input())
a, b, c, d = [None] * Q, [None] * Q, [None] * Q, [None] * Q
for q in range(Q):
    a[q], b[q], c[q], d[q] = map(int, input().split())

A = [[0] * 1501 for _ in range(1501)]
for n in range(N):
    A[Y[n]][X[n]] += 1

Z = [[0] * (1501) for _ in range(1501)]
for y in range(1, 1501):
    for x in range(1, 1501):
        Z[y][x] = A[y][x] + Z[y][x-1]
for x in range(1, 1501):
    for y in range(1, 1501):
        Z[y][x] += Z[y-1][x]

for q in range(Q):
    print(Z[d[q]][c[q]] + Z[b[q]-1][a[q]-1] - Z[b[q]-1][c[q]] - Z[d[q]][a[q]-1])