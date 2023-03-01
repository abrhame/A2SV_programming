class Solution:
    def getRow(self, rowIndex: int) -> List[int]:
        n = rowIndex
        res = [[1]]
        for i in range(n):
            temp = [1] * (2 + i)
            if i > 0:
                for j in range(i):
                    temp[j+1] = sum(res[-1][j:j+2])
                    print(res[-1])
                    print(temp)
            res.append(temp)
        print(res)
        return res[-1]