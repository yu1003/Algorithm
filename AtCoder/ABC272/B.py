N, M = map(int, input().split())
X = [input().split(' ')[1:] for _ in range(M)]

x_data = dict([[str(n+1), []] for n in range(N)])
for x_row in X:
    for x in x_row:
        x_data[x] += [x_i for x_i in x_row if x != x_i]

C = N - 1
flag = True
for x in x_data:
    if len(set(x_data[x])) != C:
        flag = False
        break
if flag == True:
    print('Yes')
else:
    print('No')