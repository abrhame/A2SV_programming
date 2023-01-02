class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        digit_chars = {
            "2" : "abc",
            "3" : "def",
            "4" : "ghi",
            "5" : "jkl",
            "6" : "mno",
            "7" : "pqrs",
            "8" : "tuv",
            "9" : "wxyz"
        }
        
        chars = [digit_chars[digit] for digit in digits]
        combs = product(*chars)
        
        result = []
        for comb in combs:
            if not comb:
                continue
            string = ''.join(comb)
            result.append(string)
        return result
                