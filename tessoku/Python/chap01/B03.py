N = int(input())
A = list(map(int, input().split()))

ans = False
for l in range(N):
    for m in range(N):
        for n in range(N):
            if (l != m) and (m != n) and (n != l):
                if (A[l] + A[m] + A[n]) == 1000:
                    ans = True

if ans == True:
    print('Yes')
else:
    print('No')