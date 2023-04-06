from collections import defaultdict
n = int(input())
list_ = defaultdict(list)
matrix = []
for i in range(n):
    row = list(map(int, input().split()))
    for j,val in enumerate(row):
        if val == 1:
            list_[i+1].append(j+1)
for key,val in list_.items():
    print(len(val),*val)

    