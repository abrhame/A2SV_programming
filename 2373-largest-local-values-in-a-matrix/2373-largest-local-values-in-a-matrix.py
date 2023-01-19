class Solution:
    def largestLocal(self, grid: List[List[int]]) -> List[List[int]]:
        n = len(grid)
        newlen = (n - 3) + 1
        maxLocal = [[] for i in range(newlen)]
        
        for row in range(newlen):
            for col in range(newlen):
                max_ = 0
                
                for i in range(row,row+3):
                    for j in range(col,col+3):
                        if grid[i][j] > max_:
                            max_ = grid[i][j]
                maxLocal[row].append(max_)
        return maxLocal
                        