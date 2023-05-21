class UnionFind:
    def __init__(self, n):
        self.parent = list(range(n))
        self.size = [1] * n
        
    def find(self, x):
        if self.parent[x] != x:
            self.parent[x] = self.find(self.parent[x])
        return self.parent[x]
    
    def union(self, x, y):
        rep_x = self.find(x)
        rep_y = self.find(y)
        if rep_x != rep_y:
            if self.size[rep_x] < self.size[rep_y]:
                self.parent[rep_x] = rep_y
                self.size[rep_y] += self.size[rep_y]
            else:
                self.parent[rep_y] = rep_x
                self.size[rep_x] += self.size[rep_y]

class Solution:
    def smallestStringWithSwaps(self, s: str, pairs: List[List[int]]) -> str:

        n = len(s)
        uf = UnionFind(n)
        components = defaultdict(list)
        for pair in pairs:
            uf.union(pair[0], pair[1])

        for i in range(n):
            root = uf.find(i)
            components[root].append(i)
        print(components)
        for indices in components.values():
            chars = [s[i] for i in indices]
            chars.sort()
            print(chars)

            for i, char in zip(indices, chars):
                s = s[:i] + char + s[i+1:]
        return s