n,m = map(int, input().split())
arr1 = list(map(int, input().split()))
arr2 = list(map(int, input().split()))

p1 = 0
p2 = 0
ans = []
while p1 < n and p2 < m:
    if arr1[p1] < arr2[p2]:
        ans.append(arr1[p1])
        p1 += 1
    else:
        ans.append(arr2[p2])
        p2 += 1
    
ans.extend(arr1[p1:])
ans.extend(arr2[p2:])
print(*ans)