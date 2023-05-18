class Solution:
    def minScore(self, n: int, roads: List[List[int]]) -> int:
        self.rep = list(range(n))
        self.weight = [float('inf')] * (n)
        self.rank = [1] * (n)

        def find(x):
            path = []
            while self.rep[x] != x:
                path.append(x)
                x = self.rep[x]

        
            for node in path:
                self.rep[node] = x
                self.weight[node] = self.weight[x]

            return x

        def union(x, y,z):
            rep_x, rep_y = find(x), find(y)
            minw = min(z,self.weight[rep_x],self.weight[rep_y])

            if rep_x != rep_y:
                if self.rank[rep_x] < self.rank[rep_y]:
                    self.rep[rep_x] = rep_y
                    self.weight[rep_x] = z
                else:
                    self.rep[rep_y] = rep_x
                    self.weight[rep_y] = z
                    if self.rank[rep_x] == self.rank[rep_y]:
                        self.rank[rep_x] += 1
            self.weight[rep_x] = minw
            self.weight[rep_y] = minw

        for a,b,c in roads:
            union(a-1,b-1,c)

        print(self.weight)
        return self.weight[find(n-1)]