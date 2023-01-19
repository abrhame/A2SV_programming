class Solution:
    def largestLocal(self, grid: List[List[int]]) -> List[List[int]]:
        n = len(grid)       # length of the grid
        newlen = (n - 3) + 1    # length of the new matrix
        maxLocal = [[] for i in range(newlen)]  # empty generated new matrix
        
        for row in range(newlen):
            for col in range(newlen):
                max_ = 0
                
                # find the local maximum value in a 3 by 3 matrix
                for i in range(row,row+3):
                    for j in range(col,col+3):
                        if grid[i][j] > max_:
                            max_ = grid[i][j]
                maxLocal[row].append(max_)
        return maxLocal
                        