t = int(input())
for _ in range(t):
    a, b = map(int, input().split())
    print(min((a+b)//4,a,b))
