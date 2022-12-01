def round_num(n, num):
    num_list = list(num)
    index = len(num_list) - n - 1
    t = int(num_list[index]) 
    num_list[index] = '0'
    if t >= 5:
        if index == 0:
            num_list = ['1'] + num_list
        else:
            num_list[index-1] = str(int(num_list[index-1])+1)
    
    for s in range(len(num_list)-1, -1, -1):
        if int(num_list[s]) >= 10:
            num_list[s] = num_list[s][1]
            if s-1 >= 0:
                num_list[s-1] = str(int(num_list[s-1])+1)
            else:
                num_list = ['1'] + num_list

    return ''.join(num_list)

X, K = map(int, input().split())
X = str(X)

for i in range(K):
    if i < len(str(X)):
        X = round_num(i, X)
    else:
        break

print(int(X))