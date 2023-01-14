class Solution:
    def matrixReshape(self, mat: List[List[int]], r: int, c: int) -> List[List[int]]:
        # if the product of r and c and the product of the orginal row and column is not equal then it is not valid to reshape the matrix
        if (len(mat) * len(mat[0])) != (r * c):
            return mat
        matrix = [[] for __ in range(r)]
        print
        a = 0
        for i in range(len(mat)):
            for j in range(len(mat[0])):
                
                # a is the index of the row
                matrix[a].append(mat[i][j])
                
                # if the length of the ath row of thw matrix is equal to the target column then move to the next row
                if len(matrix[a]) == c:
                    a +=1
        return matrix
                
            

                