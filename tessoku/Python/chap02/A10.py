N = int(input())
A = list(map(int, input().split()))
D = int(input())
L, R = [None] * D, [None] * D
for t in range(D):
    L[t], R[t] = map(int, input().split())

P = [None] * N
Q = [None] * N
P[0] = A[0]
for t in range(1, N):
    P[t] = max(P[t-1], A[t])
Q[-1] = A[-1]
for t in range(N-2, -1, -1):
    Q[t] = max(Q[t+1], A[t])

for i in range(D):
    print(max(P[L[i]-2], Q[R[i]]))