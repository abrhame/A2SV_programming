t = int(input())

for i in range(t):
    n = int(input())
    a = list(map(int, input().split()))
    j = 0
    flag = False
    a.sort()
    while j < n-1:
        abs_diff = abs(a[j] - a[j+1])
        if abs_diff > 1:
            flag = True
            break
        elif abs_diff <= 1:
                a.pop(j)
                n -= 1
        else:
            j +=1
    if flag == False and len(a) == 1:
        print('YES')
    elif flag == True or len(a) > 1:
        print('NO')
    
        