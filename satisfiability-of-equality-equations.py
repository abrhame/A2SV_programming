class Solution:
    def equationsPossible(self, equations: List[str]) -> bool:
        n = len(equations) + 1
        self.rep = {}
        self.rank = [0] * n

        def find(x):
            if x not in self.rep:
                self.rep[x] = x
                return x
            elif self.rep[x] == x:
                return x
            return find(self.rep[x])
            
        def union(x,y):
            rep_x = find(x)
            rep_y = find(y)
            if rep_x == rep_y:
                return 
            self.rep[rep_x] = rep_y
        
        for eq in equations:
            if eq[1] == "=":
                union(eq[0],eq[3])

        for eq in equations:
            if eq[1] == "!":
                if find(eq[0]) == find(eq[3]):
                    return False
        return True