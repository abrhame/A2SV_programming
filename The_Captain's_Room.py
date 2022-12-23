k = int(input())
roomList = list(map(int, input().split()))

groups = {}
res = 0

for member in roomList:
    if member in groups:
        groups[member] +=1
    else:
        groups[member] = 1
        
for group in groups:
    if groups[group] == 1:
        print(group)
