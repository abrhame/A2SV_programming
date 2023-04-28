class Solution:
    def allPathsSourceTarget(self, graph: List[List[int]]) -> List[List[int]]:
        gmap = defaultdict(list)
        for i, val in enumerate(graph):
            for v in val:
                gmap[i].append(v)
                if v not in gmap:
                    gmap[v] = []
        
        ans = []
        visited = set()
        def dfs(gmap, visited, node, tmp):
            nonlocal ans
            visited.add(node)
            if node == len(graph) - 1:
                ans.append(tmp[:])
            
            for i in gmap[node]:
                if i not in visited:
                    tmp.append(i)
                    dfs(gmap, visited, i, tmp)
                    tmp.pop()

            visited.remove(node)

        dfs(gmap, visited, 0, [0])
        return ans