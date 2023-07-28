class Solution:
    def maxSatisfaction(self, satisfaction: List[int]) -> int:
        n = len(satisfaction)

        satisfaction.sort()
        if satisfaction[-1] <= 0:
            return 0
        
        i = n-1
        temp = 0
        ans = 0
        while i >= 0 and satisfaction[i] + temp >= 0:
            temp += satisfaction[i]
            ans += temp
            i -= 1
        
        return ans