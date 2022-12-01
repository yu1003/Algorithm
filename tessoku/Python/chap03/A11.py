N, X = map(int, input().split())
A = list(map(int, input().split()))

L, R = 0, N-1
ans = None
while L <= R:
    M = (L + R) // 2
    if X == A[M]:
        ans = M + 1
        break
    elif X < A[M]:
        R = M - 1
    else:
        L = M + 1

print(ans)