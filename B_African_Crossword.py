# recive input
n,m = map(int, input().split())
mat = []
for i in range(n):
    row = list(input())
    mat.append(row)

ans = []
# transpose the matrix to cross out the repeated letters
column = []
for i in range(m):
    col = []
    for j in range(n):
        col.append(mat[j][i])
    column.append(col)
    
# iterate for each elemetn and check for they are not repeated in row wise and column wise.   
for i in range(n):
    for j in range(m):
        
        # if there element is repeated more than once in the row. jump it
        if mat[i].count(mat[i][j]) > 1:
            continue
            
        # if the elemnt is repeated more than once in the column. jump it
        if column[j].count(mat[i][j]) > 1:
            continue
            
        # if the element is not repeated in the row and column wise it is not crossed out.
        else:
            ans.append(mat[i][j])
            
print("".join(ans))
