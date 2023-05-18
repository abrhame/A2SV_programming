class Solution:
    def removeStones(self, stones: List[List[int]]) -> int:
        n = len(stones)
        self.rep = list(range(n))
        self.rank = [1] * n
        print(self.rep)
        def find(x):
            if self.rep[x] == x:
                return x
            self.rep[x] = find(self.rep[x])
            return self.rep[x]
        
        def union(x,y):
            rep_x = find(x)
            rep_y = find(y)

            if rep_x != rep_y:
                if self.rank[rep_x] < self.rank[rep_y]:
                    self.rep[rep_y] = rep_x
                else:
                    self.rep[rep_x] = rep_y
                    if self.rank[rep_x] == self.rank[rep_y]:
                        self.rank[rep_x] += 1
        
        for i in range(n):
            for j in range(i,n):
                if stones[i][0] == stones[j][0] or stones[i][1] == stones[j][1]:
                    union(i,j)
            
        count = 0
        print(self.rep)
        for i,v in enumerate(self.rep):
            if i != v:
                count += 1


        return count