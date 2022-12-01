N, Q = map(int, input().split())
A = list(map(int, input().split()))
LR = [list(map(int, input().split())) for _ in range(Q)]

C = {0:0}
for n in range(N):
    i = n + 1
    if i == 1:
        C[i] = A[n]
    else:
        C[i] = (C[i-1] + A[n])

for q in range(Q):
    L, R = LR[q]
    print(C[R] - C[L-1])