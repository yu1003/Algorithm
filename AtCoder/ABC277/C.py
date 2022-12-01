# def exp(v, G, seen, ans):
#     seen[v] = True
#     for v2 in G[v]:
#         if ans <= v2:
#             ans = v2
#         if seen[v2]: continue
#         ans = exp(v2, G, seen, ans)
#     return ans

# N = int(input())
# AB = [list(map(int, input().split())) for _ in range(N)]

# M = max([c for ab in AB for c in ab])
# G = [[] for _ in range(M+1)]
# for n in range(1, N+1):
#     A, B = AB[n-1]
#     G[A].append(B)
#     G[B].append(A)

# seen = [False for _ in range(M+1)]
# ans = 1
# ans = exp(1, G, seen, ans)
# print(ans)