class Solution:
    def findAllRecipes(self, recipes: List[str], ingredients: List[List[str]], supplies: List[str]) -> List[str]:
        
        mp = defaultdict(list)
        indegree = Counter()
        queue = deque(supplies)
        supplies = set(supplies)
        ans = []
        for i,elem in enumerate(ingredients):
            for e in elem:
                mp[e].append(recipes[i])
                indegree[recipes[i]] += 1
        
        while queue:
            node = queue.popleft()
            if node not in supplies:
                ans.append(node)
            for child in mp[node]:
                indegree[child] -= 1
                if indegree[child] == 0:
                    queue.append(child)
        return ans