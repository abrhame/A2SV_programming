class Solution:
    def hasValidPath(self, grid: List[List[int]]) -> bool:
        n = len(grid)
        m = len(grid[0])
        rep = {(i,j):(i,j) for i in range(n) for j in range(m)}
        size = {(i,j):1 for i in range(n) for j in range(m)}
        
        d = {
            1: set([(0,1),(0,-1,)]),
            2: set([(1,0),(-1,0)]),
            3: set([(0,-1),(1,0)]),
            4: set([(0,1),(1,0)]),
            5: set([(-1,0),(0,-1)]),
            6: set([(-1,0),(0,1)])
        }    

        def inbound(x,y):
            return  0 <= x < n and 0 <= y < m

        def find(x):
            if rep[x] == x:
                return x
 
            rep[x] = find(rep[x])
            return rep[x]
        
        def union(x, y):
            rep_x = find(x)
            rep_y = find(y)
            if rep_x == rep_y:
                return [x,y]
            if size[rep_x] > size[rep_y]:
                rep[rep_y] = rep[rep_x]
                size[rep_x]+=size[rep_y]
            else:
                rep[rep_x] = rep[rep_y]
                size[rep_y]+=size[rep_x]
            return None
        
        def connected(x,y):
            return find(x) == find(y)
            
        
        for i in range(n):
            for j in range(m):
                curr = grid[i][j]
                for x,y in d[curr]:
                    nr = i + x
                    nc = j + y

                    if inbound(nr,nc):
                        new = grid[nr][nc]

                        if (-x,-y) in d[new]:
                            union((nr,nc),(i,j))
        
        return connected((0,0),(n - 1,m - 1))