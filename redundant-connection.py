class Solution:
    def findRedundantConnection(self, edges: List[List[int]]) -> List[int]:
        n = len(edges) + 1
        self.rep = list(range(n))
        self.rank = [1] * (n)

        def find(x):
            while x != self.rep[x]: 
                x = self.rep[x]
            return x

        def union(x, y):
            rep_x, rep_y = find(x), find(y)

            if rep_x == rep_y:
                return False
            elif self.rank[rep_x] < self.rank[rep_y]:
                    self.rep[rep_x] = rep_y
            else:
                self.rep[rep_y] = rep_x
                if self.rank[rep_x] == self.rank[rep_y]:
                    self.rank[rep_x] += 1
            return True

        def solve(edges):
            for a, b in edges:
                if not union(a, b):
                    return [a,b]

            
        return solve(edges)