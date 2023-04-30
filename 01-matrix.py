class Solution:
    def updateMatrix(self, mat: List[List[int]]) -> List[List[int]]:
        queue = deque()
        visited = set()   
        directions = [(1,0),(0,1),(-1,0),(0,-1)] 

        def inbound(i,j):
            return (0<= i < len(mat)) and (0<= j < len(mat[0]))

        def solve():
            count = 0
            while queue:
                n = len(queue)
                count += 1
                for _ in range(n):
                    i,j = queue.popleft()
                    for x,y in directions:
                        n_i = x + i
                        n_j = y + j

                        if inbound(n_i,n_j) and (n_i,n_j) not in visited and mat[n_i][n_j] == 1:
                            queue.append((n_i,n_j))
                            visited.add((n_i,n_j))
                            mat[n_i][n_j] = count
        
        for i in range(len(mat)):
            for j in range(len(mat[0])):
                if mat[i][j] == 0:
                    queue.append((i,j))
                    visited.add((i,j))
        solve()
        return mat