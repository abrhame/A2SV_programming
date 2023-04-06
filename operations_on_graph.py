from collections import defaultdict
n = int(input())
k = int(input())

matrix = defaultdict(list)

for i in range(k):
    a = list(map(int, input().split()))
    if a[0] == 1:
        matrix[a[1]].append(a[2])
        matrix[a[2]].append(a[1])
    if a[0] == 2:
        # print(matrix)
        if a[1] > n:
            print()
        else:
            print(*matrix[a[1]])