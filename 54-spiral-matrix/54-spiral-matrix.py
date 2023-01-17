class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        cb = 0
        ce = len(matrix[0]) - 1
        rb = 0
        re = len(matrix) - 1
        ans = []
        if len(matrix) == 0:
            return ans
        while rb <= re and cb <= ce:
            for i in range(cb,ce+1):
                ans.append(matrix[rb][i])
            rb += 1
            
            for i in range(rb,re+1):
                ans.append(matrix[i][ce])
            ce -= 1
            
            if rb <= re:
                for i in range(ce,cb-1,-1):
                    ans.append(matrix[re][i])
                re -= 1
            
            if cb <= ce:    
                for i in range(re,rb - 1, -1):
                    ans.append(matrix[i][cb])
                cb +=1  
            
        return ans
       
                
        