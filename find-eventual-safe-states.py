class Solution:
    def eventualSafeNodes(self, graph: List[List[int]]) -> List[int]:
            colors = [0] * len(graph)
            res = []
            
            def dfs(node):
                if colors[node] == 1: 
                    return False
                if colors[node] == 2: 
                    return True
                
                colors[node] = 1
                
                for neighbor in graph[node]:
                    if not dfs(neighbor):
                        return False
                
                colors[node] = 2
                return True
            
            for node in range(len(graph)): 
                if dfs(node):
                    res.append(node)
            
            return res