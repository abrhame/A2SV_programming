eStudents = int(input())
eStudentsList = set(map(int, input().split()))

fStudents = int(input())
fStudentsList = set(map(int, input().split()))

size = len(eStudentsList.difference(fStudentsList))
print(size)
