H, W = map(int, input().split())
X = [list(map(int, input().split())) for _ in range(H)]
Q = int(input())
ABCD = [list(map(int, input().split())) for _ in range(Q)]

Z = [[0 for _ in range(W+1)] for _ in range(H+1)]
for h in range(1, H+1):
    for w in range(1, W+1):
        Z[h][w] = X[h-1][w-1] + Z[h][w-1]
for w in range(1, W+1):
    for h in range(1, H+1):
        Z[h][w] += Z[h-1][w]

for q in range(1, Q+1):
    A, B, C, D = ABCD[q-1]
    ans = Z[C][D] + Z[A-1][B-1] - Z[C][B-1] - Z[A-1][D]
    print(ans)