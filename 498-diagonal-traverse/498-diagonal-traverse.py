class Solution:
    def findDiagonalOrder(self, mat: List[List[int]]) -> List[int]:
        ind = {}
        for i in range(len(mat)):
            for j in range(len(mat[i])):
                if i + j not in ind:
                    ind[i+j] = [mat[i][j]]
                else:
                    ind[i+j].append(mat[i][j])

        ans = []
        for entry in ind.items():
            if entry[0] % 2 == 0:
                for element in entry[1][::-1]:
                    ans.append(element)
            else:
                for element in entry[1]:
                    ans.append(element)
        return ans