class Solution:
    def findSmallestSetOfVertices(self, n: int, edges: List[List[int]]) -> List[int]:
        ans = [True] * n
        res = []
        for i,val in enumerate(edges):
            ans[val[1]] = False

        for i,val in enumerate(ans):
            if val == True:
                res.append(i)
        return res