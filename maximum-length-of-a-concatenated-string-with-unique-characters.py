class Solution:
    def maxLength(self, arr: List[str]) -> int:
        string = ""
        length = 0
        def bt(string):
            nonlocal length
            if len(string) != len(set(string)):
                return
            length = max(length,len(string))
            for i in range(len(arr)):
                
                bt(string+arr[i])

        bt(string)
        return length