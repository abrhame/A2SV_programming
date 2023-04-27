class Solution:
    def shortestPathBinaryMatrix(self, grid: List[List[int]]) -> int:

        if grid[0][0] == 1 or grid[len(grid)-1][len(grid)-1] == 1:
            return -1
        queue = deque()
        queue.append((0,0))
        grid[0][0] = 1
        directions = [(0,1),(1,0),(0,-1),(-1,0),(1,1),(-1,-1),(1,-1),(-1,1)]
        count = 0
        def inbound(i,j):
            return (0 <= i < len(grid)) and (0<= j < len(grid[0]))
        while queue:
            n = len(queue)
            count += 1
            for _ in range(n):
                i,j = queue.popleft()
                if (i,j) == (len(grid)-1, len(grid)-1):
                    return count
                for x,y in directions:
                    n_i = i + x
                    n_j = j + y
                    if inbound(n_i,n_j) and grid[n_i][n_j] == 0:
                        grid[n_i][n_j] = 1
                        queue.append((n_i,n_j))
        
        return -1