t = int(input())
for i in range(t):
    first, second = input().split()
    f = first.count("X") 
    s = second.count("X")
    if first == second:
        print("=")
    elif first[-1] == "M" and second[-1] == "S":
        print(">")
    elif first[-1] == "L" and (second[-1] == "S" or second[-1] == "M"):
        print(">")
    elif first[-1] == "S" and (second[-1] == "L" or second[-1] == "M"):
        print("<")
    elif first[-1] == "M" and second[-1] == "L":
        print("<")
    elif (first[-1] == "L" and second[-1] == "L") and (f > s):
        print(">")
    elif (first[-1] == "L" and second[-1] == "L") and (f < s):
        print("<")
    elif (first[-1] == "S" and second[-1] == "S") and (f > s):
        print("<")
    elif (first[-1] == "S" and second[-1] == "S") and (f < s):
        print(">")
