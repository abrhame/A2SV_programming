n=int(input())
a=list(map(int,input().split()))

# Notice that you can only swap 2 elements if they have different parities. 
# If all elements in the array have the same parity, you can't do any swaps, and the answer will just be like the input.
odd=0;even=0
for num in a:
          if num%2: 
              odd=1
          else:
              even=1
if odd and even:
          print(*sorted(a))
else:
    print(*a)
        