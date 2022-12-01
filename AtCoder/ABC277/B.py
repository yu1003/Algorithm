N = int(input())
S = [input() for _ in range(N)]

ans = True
for n in range(N):
    if S[n][0] not in ['H', 'D', 'C', 'S']:
        ans = False
        break
    else:
        if S[n][1] not in ['A', '2', '3', '4', '5', '6', '7', '8', '9', 'T', 'J', 'Q', 'K']:
            ans = False
            break

if ans == True:
    if len(set(S)) == N:
        print('Yes')
    else:
        print('No')
else:
    print('No')