A = set(map(int, input().split()))
n = int(input())
result = []
for i in range(n):
    B = set(map(int, input().split()))
    if not A.issuperset(B):
        result.append(False) 
    else:
        result.append(True)
print(bool(not(False in result)))
