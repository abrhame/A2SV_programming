n = int(input())
source = []
sink = []
matrix = []
for i in range(n):
    row = list(map(int, input().split()))
    if row.count(1) == 0:
        sink.append(i+1)
    matrix.append(row)
    
for i, val in enumerate(zip(*matrix)):
    if list(val).count(1) == 0:
        source.append(i + 1)

print(len(source), *source)
print(len(sink), *sink)


