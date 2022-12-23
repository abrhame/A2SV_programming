n, m = map(int, input().split()) 
arr = list(map(int, input().split()))
A = set(map(int, input().split()))
B = set(map(int, input().split()))

# the first line is array of integer which contains the lwength of the arrays of the integers and the the sets respectively
#if the integers in arr are the subset of the sets we add 1 to our hapiness

##solution iterate over the arr array and if that is the subset of A add 1 to your hapiness. if it is not subtract one from your hapiness
happy = 0
for num in arr:
    if num in A:
        happy += 1
    elif num in B:
        happy -=1

print(happy)
