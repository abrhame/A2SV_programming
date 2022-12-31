class Solution:
    def onesMinusZeros(self, grid: List[List[int]]) -> List[List[int]]:
        m, n = len(grid), len(grid[0])

        def count(nums): return 2*(sum(nums)) - len(nums)

        r = list(map(count, grid))
        c = list(map(count, zip(*grid))) # transpose

        for i, j in product(range(m), range(n)):
            grid[i][j] = r[i] + c[j]
        
        return grid
#         onesRows = collections.defaultdict(int)
#         onesCols = collections.defaultdict(int)
#         zerosRows = collections.defaultdict(int)
#         zerosCols = collections.defaultdict(int)
        
#         for i, row in enumerate(grid):
#             for j, cell in enumerate(row):
#                 if cell == 1:
#                     onesRows[i] +=1
#                     onesCols[j] +=1
#                 else:
#                     zerosRows[i] +=1
#                     zerosCols[j] +=1
                    
#         rows, cols = len(grid), len(grid[0])
#         diff = [[0 for _ in range(cols)] for _ in range(rows)]
        
#         for i in range(rows):
#             for j in range(cols):
#                 diff[i][j] = onesRows[i] + onesCols[j] - zerosRows[i] - zerosCols[j]
#         return diff
