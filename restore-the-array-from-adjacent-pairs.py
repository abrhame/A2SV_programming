class Solution:
    def restoreArray(self, adjacentPairs: List[List[int]]) -> List[int]:
        graph = defaultdict(list)
        indegree = {}
        queue = deque()
        ans = []
        visited = set()
        for x,y in adjacentPairs:
            graph[x].append(y)
            graph[y].append(x)
           

        for k,v in graph.items():
            if len(v) == 1:
                queue.append(k)
                break
        

    
        while queue:
            node = queue.popleft()
            visited.add(node)
            ans.append(node)
            for child in graph[node]:
                if child not in visited:
                    queue.append(child)

        return ans