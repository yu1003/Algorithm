D = int(input())
N = int(input())
LR = [list(map(int, input().split())) for _ in range(N)]

B = [0] * (D + 2)
for n in range(1, N+1):
    L, R = LR[n-1]
    B[L] += 1
    B[R+1] -= 1

C = 0
for d in range(1, D+1):
    C = C + B[d]
    print(C)