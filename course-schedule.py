class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        graph = defaultdict(list)
        countIncoming = {i:0 for i in range(numCourses)}
        topological_sort = []
        for x,y in prerequisites:
            graph[y].append(x)
        

        for k in graph:
            for elem in graph[k]:
                countIncoming[elem] += 1
        
        queue = deque()
        seen = set()
        for k,v in countIncoming.items():
            if v == 0:
                queue.append(k)
        
        while queue:
            node = queue.popleft()
            topological_sort.append(node)
            for child in graph[node]:
                countIncoming[child] -= 1

                if countIncoming[child] == 0:
                    queue.append(child)
            
        if len(topological_sort) != numCourses:
            return False
        return True