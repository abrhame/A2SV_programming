class Solution:
    def validPath(self, n: int, edges: List[List[int]], source: int, destination: int) -> bool:
        self.rep = list(range(n))
        self.rank = [1] * n

        def find(x):
            path = []
            while x != self.rep[x]:
                path.append(x)
                x = self.rep[x]

            # Path compression: Update parent pointers
            for node in path:
                self.rep[node] = x

            return x

        def union(x, y):
            rep_x, rep_y = find(x), find(y)

            if rep_x != rep_y:
                if self.rank[rep_x] < self.rank[rep_y]:
                    self.rep[rep_x] = rep_y
                else:
                    self.rep[rep_y] = rep_x
                    if self.rank[rep_x] == self.rank[rep_y]:
                        self.rank[rep_x] += 1

        def solve(edges, s, d):
            for a, b in edges:
                union(a, b)

            return find(s) == find(d)

        return solve(edges, source, destination)