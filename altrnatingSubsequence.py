t = int(input())

for ___ in range(t):
    n = int(input())
    a = list(map(int, input().split()))
    
    up = False
    down = False
    ans = 0

    if a[0] < 0:
        down = True
    else:
        up = True
    j = 0
    for i in range(1,n):
        if down and a[i] > 0:
            down = False
            up = True

            ans += max(a[j:i])
            j = i
        elif up and a[i] < 0:
            up = False
            down = True
            ans += max(a[j:i])
            j = i
    ans += max(a[j:])
    print(ans)

