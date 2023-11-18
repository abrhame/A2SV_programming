class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        if digits[-1] == 9:
            if len(digits) == 1:
                return [1,0]
            return self.plusOne(digits[:-1]) + [0]
        else:
            digits[-1] += 1
        return digits
                

            
            
            
            
            
#         ans = ""
#         for num in digits:
#             ans += str(num)
#         ans = int(ans)+1
#         ans = list(str(ans))
#         res = []
#         for num in ans:
#             res.append(int(num))
            
#         return res