class Solution:
    def matrixReshape(self, mat: List[List[int]], r: int, c: int) -> List[List[int]]:
        if (len(mat) * len(mat[0])) != (r * c):
            return mat
        matrix = [[] for __ in range(r)]
        print
        a = 0
        for i in range(len(mat)):
            for j in range(len(mat[0])):
                matrix[a].append(mat[i][j])
                if len(matrix[a]) == c:
                    a +=1
        return matrix
                
            

                