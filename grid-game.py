class Solution:
    def gridGame(self, grid: List[List[int]]) -> int:
        row1_prefix = [grid[0][0]]
        row2_prefix = [grid[1][0]]
        n = len(grid[0])
        res = float('inf')
        for i in range(1,n):
            row1_prefix.append(row1_prefix[i-1] + grid[0][i])
            row2_prefix.append(row2_prefix[i-1] + grid[1][i])

        for i in range(n):
            row1 = row1_prefix[-1] - row1_prefix[i]
            row2 = row2_prefix[i-1] if i > 0 else 0
            second_robot = max(row1,row2)
            res = min(res,second_robot)
        return res