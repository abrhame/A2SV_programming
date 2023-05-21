class Solution:
    def shortestBridge(self, grid: List[List[int]]) -> int:
        directions = [(0,1),(-1,0),(1,0),(0,-1)]
        visited = set()
        count = -1
        def inbound(i,j):
            return (0 <= i < len(grid)) and (0 <= j < len(grid[0]))

        def dfs(i,j):
            visited.add((i,j))
            grid[i][j] = 2
            for x,y in directions:
                nr = i + x
                nc = j + y
                if inbound(nr,nc) and grid[nr][nc] == 1:
                    dfs(nr,nc)
                    
                
        
        def bfs(visited):
            nonlocal count
            visited = list(visited)
            queue = deque()
            for node in visited:
                queue.append(node)
            print(queue)
            while queue:
                n = len(queue)
                count += 1
                for _ in range(n):
                    i,j = queue.popleft()
                    for x,y in directions:
                        nr = i + x
                        nc = j + y
                        if inbound(nr,nc):
                            if grid[nr][nc] == 1:
                                return count
                            if grid[nr][nc] == 0:
                                queue.append((nr,nc))
                                grid[nr][nc] = 2
        flag = False
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] == 1:
                    dfs(i,j)
                    grid[i][j] = 2
                    flag = True
                    break
            if flag == True:
                break
        bfs(visited)
        return count