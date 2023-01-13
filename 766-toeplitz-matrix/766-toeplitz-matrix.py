class Solution:
    def isToeplitzMatrix(self, matrix: List[List[int]]) -> bool:
        diag = defaultdict(list)
        
        for i in range(len(matrix)):
            for j, value in enumerate(matrix[i]):
                if len(diag[i-j]) == 0:
                    diag[i-j].append(value)
                elif diag[i-j][0] != value:
                    return False
        return True