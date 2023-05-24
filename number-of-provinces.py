class Solution:
    def dfs(self, node: int, isConnected: List[List[int]], visit: List[bool]) -> None:
        visit[node] = True
        for i in range(len(isConnected)):
            if isConnected[node][i] == 1 and not visit[i]:
                self.dfs(i, isConnected, visit)

    def findCircleNum(self, isConnected: List[List[int]]) -> int:
        n = len(isConnected)
        numberOfComponents = 0
        visit = [False] * n

        for i in range(n):
            if not visit[i]:
                numberOfComponents += 1
                self.dfs(i, isConnected, visit)

        return numberOfComponents