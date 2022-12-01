n, a, b = map(int, input().split())

all_wa = 0
for i in range(1,n+1):
    i_str = str(i)
    wa = 0
    for m in range(len(i_str)):
        wa += int(i_str[m])
    if wa >= a and wa <= b:
        all_wa += i
        
print(all_wa)