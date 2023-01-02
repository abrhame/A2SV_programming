class Solution:
    def addSpaces(self, s: str, spaces: List[int]) -> str:
            answer = []
            prev = 0
            
            for space in spaces:
                answer.append(s[prev:space])
                prev = space
            answer.append(s[space:])
            
            return " ".join(answer)
            