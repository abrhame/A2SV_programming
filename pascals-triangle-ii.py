class Solution:
    def getRow(self, rowIndex: int) -> List[int]:
        
        def pascal(row,n):
            if n == rowIndex:
                return row 
            temp = [1] * (2 + n)

            if len(row) >=2:
                for j in range(len(row)):
                    temp[j+1] = sum(row[j:j+2])

            return pascal(temp,n+1)
        return pascal([1],0)
        

            




        # n = rowIndex
        # res = [[1]]
        # for i in range(n):
        #     temp = [1] * (2 + i)
        #     if i > 0:
        #         for j in range(i):
        #             temp[j+1] = sum(res[-1][j:j+2])
        #     res.append(temp)
        # return res[-1]