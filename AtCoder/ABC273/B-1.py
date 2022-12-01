X, K = map(int, input().split())

for i in range(1, K+1):
    if len(str(X)) < i:
        break
    if str(X)[-i] == '5':
        x = list(str(X))
        x[-i] = str(int(x[-i]) + 1)
        X = int(''.join(x))
    X = round(X, -i)

print(X)