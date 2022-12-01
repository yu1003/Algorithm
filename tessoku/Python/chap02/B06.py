N = int(input())
A = list(map(int, input().split()))
Q = int(input())
LR = [list(map(int, input().split())) for _ in range(Q)]

CW, CL = [None] * (N+1), [None] * (N+1)
CW[0], CL[0] = 0, 0
for n in range(N):
    i = n + 1
    if A[n] == 1:
        CW[i], CL[i] = CW[i-1] + 1, CL[i-1]
    else:
        CW[i], CL[i] = CW[i-1], CL[i-1] + 1

for q in range(Q):
    L, R = LR[q]
    w = CW[R] - CW[L-1]
    l = CL[R] - CL[L-1]
    if w > l:
        print('win')
    elif w == l:
        print('draw')
    else:
        print('lose')