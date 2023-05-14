from sys import stdin, stdout

n, k = map(int, stdin.readline().split())
arr = list(map(int, stdin.readline().split()))

def solve(l, r):
    if r - l == 1:
        return [l]

    mid = (l + r) // 2
    left = solve(l, mid)
    right = solve(mid, r)


    merged = []
    l_ptr = r_ptr = 0
    left_min, right_min = arr[left[0]], arr[right[0]]

    while l_ptr < len(left) and r_ptr < len(right):
        if arr[left[l_ptr]] <= arr[right[r_ptr]]:
            if right_min - arr[left[l_ptr]] <= k:
                merged.append(left[l_ptr])
            l_ptr += 1
        else:
            if left_min - arr[right[r_ptr]] <= k:
                merged.append(right[r_ptr])
            r_ptr += 1
    while l_ptr < len(left) and right_min - arr[left[l_ptr]] <= k:
        merged.append(left[l_ptr])
        l_ptr += 1

    while r_ptr < len(right) and left_min - arr[right[r_ptr]] <= k:
        merged.append(right[r_ptr])
        r_ptr += 1
    return merged
result = solve(0, 2**n)
ans = sorted([x + 1 for x in result])
print(*ans)
