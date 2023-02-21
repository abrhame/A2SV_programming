class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        ans = ""
        for num in digits:
            ans += str(num)
        ans = int(ans)+1
        ans = list(str(ans))
        res = []
        for num in ans:
            res.append(int(num))
            
        return res