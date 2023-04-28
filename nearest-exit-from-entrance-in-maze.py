class Solution:
    def nearestExit(self, maze: List[List[str]], entrance: List[int]) -> int:
        queue = deque()
        queue.append(entrance)
        visited = set()
        visited.add(tuple(entrance))
        directions = [(1,0),(0,1),(0,-1),(-1,0)]
        count = 0
        def inbound(i, j):
            return (0<= i < len(maze)) and ( 0 <= j < len(maze[0]))
        while queue:
            n = len(queue)
            count += 1
            for _ in range(n):
                i, j = queue.popleft()
                for x,y in directions:
                    n_i = x + i
                    n_j = y + j
                    if inbound(n_i,n_j) and (n_i, n_j) not in visited and maze[n_i][n_j] == "." and ((0 == n_i or n_i == len(maze) - 1) or (0 == n_j or n_j == len(maze[0]) - 1)):
                        print(n_i,n_j)
                        print(visited)
                        return count
                    if inbound(n_i,n_j) and maze[n_i][n_j] == "." and (n_i,n_j) not in visited:
                        queue.append([n_i,n_j])
                        visited.add((n_i,n_j))
        return -1