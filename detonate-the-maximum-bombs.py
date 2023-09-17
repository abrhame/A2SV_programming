class Solution:
    def maximumDetonation(self, bombs: List[List[int]]) -> int:
        n = len(bombs)

        bwsr = defaultdict(set)
        ans = 0

        # find all the bombs that are with in the same radius(build the graph)
        for i in range(n):
            xi,yi,ri = bombs[i]

            for j in range(n):
                if i == j: continue
                xj,yj,rj = bombs[j]

                if ri ** 2 >= (xi - xj) ** 2 + (yi - yj) ** 2:
                    bwsr[i].add(j)

        def dfs(i):
            if i in seen:
                return
            seen.add(i)

            for j in bwsr[i]:
                dfs(j)

        # find all the bombs that deotnate by a single bomb
        for i in range(n):
            seen = set() 
            dfs(i)
            ans = max(ans,len(seen))

        return ans