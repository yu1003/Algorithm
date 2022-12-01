H, W = map(int, input().split())
C = [input() for _ in range(H)]

for j in range(W):
    sm = 0
    for i in range(H):
        sm += C[i][j] == '#'
    print(sm)