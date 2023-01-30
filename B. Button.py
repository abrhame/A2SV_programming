t = int(input())
for i in range(t):
    s = input()
    n = len(s)
    l = 0
    res = set()
    if len(s) == 1:
        res.add(s)
    while l < n-1:
        # move tw steps if the neboring are the same
        if s[l] == s[l+1]:
            l+=2
        # if the neiboring are not same add the ch to ans and move one step
        elif s[l] != s[l+1]:
            res.add(s[l])
            l+=1

        if l+1 == n:
            res.add(s[l])

    if len(res) == 0:
        res.add("")
    ans = sorted(res)
    ans = "".join(ans)
    print(ans)
    # res.sort()
    # res = "".join(res)
    # print(res)
    
