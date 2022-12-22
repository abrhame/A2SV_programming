from collections import deque

def pilling(cubes):
    large = 0 
    while cubes:
        if cubes[-1]>cubes[0]:
            large = cubes.pop()
        else:
            large = cubes.popleft()
        if len(cubes) == 0:
            return "Yes"
        elif cubes[-1] > large or cubes[0] > large:
            return "No"

            
for num in range(int(input())):
    n = int(input())
    cubes = deque(map(int, input().split()))
    print(pilling(cubes))
