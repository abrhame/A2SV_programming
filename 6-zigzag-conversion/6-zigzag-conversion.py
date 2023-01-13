class Solution:
    def convert(self, s: str, numRows: int) -> str:
        if numRows == 1:
            return s
        row = 0
        step = 0
        ans = [""] * numRows
        for i in range(len(s)):
            ans[row]+=(s[i])
            
            if row == 0:
                step = 1
            elif row == (numRows - 1):
                step = -1
            
            row += step
        ans = "".join(ans)
        return ans
            
            