H, W, N = map(int, input().split())
A, B, C, D = [None] * N, [None] * N, [None] * N, [None] * N
for n in range(N):
    A[n], B[n], C[n], D[n] = map(int, input().split())

T = [[0] * (W+2) for _ in range(H+2)]
Z = [[0] * (W+2) for _ in range(H+2)]
for n in range(N):
    a, b, c, d = A[n], B[n], C[n], D[n]
    T[a][b] += 1
    T[a][d+1] -= 1
    T[c+1][b] -= 1
    T[c+1][d+1] += 1

for h in range(1, H+1):
    for w in range(1, W+1):
        Z[h][w] = T[h][w] + Z[h][w-1]

for w in range(1, W+1):
    for h in range(1, H+1):
        Z[h][w] += Z[h-1][w]

for h in range(1, H+1):
    print(' '.join([str(z) for z in Z[h][1:W+1]]))