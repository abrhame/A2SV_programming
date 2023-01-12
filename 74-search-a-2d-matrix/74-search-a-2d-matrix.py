class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        arr = []
        for i in range(len(matrix)):
            if target <= matrix[i][-1]:
                arr = matrix[i]
                break
        if target in arr:
            return True
        else:
            return False
        