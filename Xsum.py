t = int(input())
for i in range(t):
    n,m = map(int, input().split())
    matrix = []
    for j in range(n):
        row = list(map(int, input().split()))
        matrix.append(row)
    diag = [0] * (n + m -1)
    anti_diag = [0] * (n + m -1)
    offset = m - 1
    for i in range(n):
        for j, value in enumerate(matrix[i]):
            diag[i-j + offset] += value
            anti_diag[i+j] += value
    maximum = 0
    for i in range(n):
        for j,value in enumerate(matrix[i]):
            maximum = max(maximum,(diag[i - j + offset] + anti_diag[j + i] - value))
    print(maximum)
