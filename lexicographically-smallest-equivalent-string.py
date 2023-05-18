class Solution:
    def smallestEquivalentString(self, s1: str, s2: str, baseStr: str) -> str:
        self.rep = {}
        for i in range(27):
            temp = chr(i+ord("a"))
            self.rep[temp] = temp
        print(self.rep)
        def find(x):
            if x not in self.rep:
                self.rep[x] = x
                return x
            elif self.rep[x] == x:
                return x
            self.rep[x] = find(self.rep[x])
            return self.rep[x]

        def union(x,y):
            rep_x = find(x)
            rep_y = find(y)

            if rep_x == rep_y:
                return
            self.rep[rep_y] = rep_x


        for i in range(len(s1)):
            p = find(s1[i])
            q = find(s2[i])
            if p > q:
                union(q,p)
            else:
                union(p,q)
        ans = []
        print(self.rep)
        for i in range(len(baseStr)):
            ans.append(find(baseStr[i]))
        
        return "".join(ans)