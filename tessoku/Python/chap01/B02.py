A, B = map(int, input().split())

ans = False
for i in range(A, B+1):
    if 100 % i == 0:
        ans = True
        break

if ans == True:
    print('Yes') 
else:
    print('No')