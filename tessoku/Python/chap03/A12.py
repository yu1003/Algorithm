# def search(N, K, A):
#     L, R = 1, 10 ** 9
#     while L < R:
#         M = (L + R) // 2

#         flag = check(K, A, M)
#         if flag == 0:
#             return M
#         elif flag == 1:
#             L = M + 1
#         else:
#             R = M - 1
        
#     return R

# def check(K, A, M):
#     s = 0
#     for i in range(N):
#         s += M // A[i]
    
#     if s == K:
#         flag = 0
#     elif s < K:
#         flag = 1
#     else:
#         flag = -1

#     return flag

# N, K = map(int, input().split())
# A = list(map(int, input().split()))

# print(search(N, K, A))