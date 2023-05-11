class Solution:
    def getAncestors(self, n: int, edges: List[List[int]]) -> List[List[int]]:
        graph = defaultdict(list)
        indegree = [0] * n
        queue = deque()
        ans = [set() for i in range(n)]
        for b, a in edges:
            graph[b].append(a)
            indegree[a] += 1
        print(indegree)
        print(graph)
        for i in range(len(indegree)):
            if indegree[i] == 0:    
                queue.append(i)
        print(queue)
        while queue:
            node = queue.popleft()

            for child in graph[node]:
                indegree[child] -= 1
                ans[child].add(node)
                for i in ans[node]:
                    ans[child].add(i)
                if indegree[child] == 0:
                    queue.append(child)
        
        ans_ = []

        for v in ans:
            ans_.append(sorted(v))
        

        return ans_