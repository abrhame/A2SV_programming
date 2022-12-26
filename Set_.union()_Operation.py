eStudents = int(input())
eStudentsList = set(map(int, input().split()))

fStudents = int(input())
fStudentsList = set(map(int, input().split()))

total = len(eStudentsList.union(fStudentsList))

print(total)
