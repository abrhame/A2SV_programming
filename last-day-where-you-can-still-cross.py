class Solution:
    def latestDayToCross(self, row: int, col: int, cells: List[List[int]]) -> int:
        mat = [ [1] * col for i in range(row)]
        parent = { (i, j): [(i, j), i, i] for i in range(row) for j in range(col)}
        dirc = [(1, 0), (0, 1), (0, -1), (-1, 0)]

        def find(node):
            if node != parent[node][0]:
                parent[node][0] = find(parent[node][0])
            return parent[node][0]

        def union(node1, node2):
            par1 = find(node1) #[ parent, minRow, maxRow]
            par2 = find(node2)
            if par1 != par2:

                minRow = min(parent[par1][1], parent[par2][1])
                maxRow = max(parent[par1][2], parent[par2][2])
                parent[par1] = [par2, minRow, maxRow]
                parent[par2][1] = minRow
                parent[par2][2] = maxRow
                if maxRow - minRow == row - 1:
                    return True
            
            return False
                
        
        for k in range(len(cells) - 1, -1, -1):
            i, j = cells[k]
            i -= 1
            j -= 1
            mat[i][j] = 0
            for x, y in dirc:
                nr, nc = i + x, j + y
                if 0 <= nr < row and 0 <= nc < col and mat[nr][nc] == 0:
                    if union((nr, nc), (i, j)):
                        return k

        return 0