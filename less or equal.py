n,k = map(int, input().split())
a = list(map(int, input().split()))
a.sort()

if k == 0:
    print(a[k]-1) if a[k] > 1 else print(-1)
elif k == len(a) or (0<k<len(a) and a[k-1] != a[k]):
    print(a[k-1])
else:
    print(-1)
