class Solution:
    def balancedStringSplit(self, s: str) -> int:
        check = []
        answer = 0
        ap = s[0]

        for i in s:
            if len(check) == 0:
                answer += 1
                ap = i
            
            if i == ap:
                check.append(i)
            elif len(check) != 0:
                check.pop()
            
            
            
        return answer