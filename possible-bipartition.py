class Solution:
    def possibleBipartition(self, n: int, dislikes: List[List[int]]) -> bool:
        graph = defaultdict(list)
        for k,v in dislikes:
            graph[k].append(v)
            graph[v].append(k)
        visited = set()
        color = [None for _ in range(n+1)]

        def dfs(graph,v,color,visited):
            visited.add(v)
            for u in graph[v]:
                if u not in visited:
                    color[u] = not color[v] if color[v] is not None else True
                    if (not dfs(graph,u,color,visited)):
                        return False
                elif (color[u] == color[v]):
                    return False
            return True
        
        for i in range(1, n+1):
            if i not in visited:
                color[i] = True
                if not dfs(graph,i,color,visited):
                    return False
        return True