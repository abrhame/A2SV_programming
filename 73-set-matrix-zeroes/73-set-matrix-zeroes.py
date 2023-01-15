class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        zeros = []
        for i in range(len(matrix)):
            for j in range(len(matrix[0])):
                if matrix[i][j] == 0:
                    zeros.append([i,j])
        # setting the row to zero
        for i in range(len(zeros)):
            for j in range(len(matrix[0])):     # set all the column values to zero
                matrix[zeros[i][0]][j] = 0
        
        # setting the column to zero
        for i in range(len(zeros)):
            for j in range(len(matrix)):     # set all the row values to zero
                matrix[j][zeros[i][1]] = 0
        
        return matrix