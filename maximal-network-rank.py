class Solution:
    def maximalNetworkRank(self, n: int, roads: List[List[int]]) -> int:
        ans = 0
        graph = defaultdict(set)
        for x,y in roads:
            graph[x].add(y)
            graph[y].add(x)
        # print(graph)
        for k,v in graph.items():
            for i,j in graph.items():
                if k != i:
                    minus = 0
                    if k in j:
                        minus = 1
                    temp = len(v) + len(j) - minus
                    ans = max(ans,temp)
        return ans