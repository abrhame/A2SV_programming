n = int(input())
count = 0

for i in range(n):
    inp = list(map(int, input().split()))
    count += inp.count(1)
print(count//2)