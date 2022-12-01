N, X = map(int, input().split())
A = list(map(int, input().split()))

ans = False
for i in range(N):
    if A[i] == X:
        ans = True 
        break
    
if ans == True:
    print('Yes')
else:
    print('No')