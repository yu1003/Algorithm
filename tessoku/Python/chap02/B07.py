T = int(input())
N = int(input())
LR = [list(map(int, input().split())) for _ in range(N)]

B = [0] * (T + 1)
for n in range(1, N+1):
    L, R = LR[n-1]
    B[L] += 1
    B[R] -= 1

C = 0
for t in range(T):
    C = C + B[t]
    print(C)