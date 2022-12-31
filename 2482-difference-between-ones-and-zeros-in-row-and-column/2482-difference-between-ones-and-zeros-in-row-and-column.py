class Solution:
    def onesMinusZeros(self, grid: List[List[int]]) -> List[List[int]]:
        m, n = len(grid), len(grid[0])

        def count(nums): 
            return 2*(sum(nums)) - len(nums)

        r = list(map(count, grid))
        c = list(map(count, zip(*grid))) # transpose

        for i, j in product(range(m), range(n)):
            grid[i][j] = r[i] + c[j]
        
        return grid

