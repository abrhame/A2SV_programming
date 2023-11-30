class Solution:
    def transpose(self, matrix: List[List[int]]) -> List[List[int]]:
        n, m = len(matrix), len(matrix[0])
        return [[matrix[i][j] for i in range(n)] for j in range(m)]

        