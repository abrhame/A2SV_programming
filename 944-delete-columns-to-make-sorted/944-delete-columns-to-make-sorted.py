class Solution:
    def minDeletionSize(self, strs: List[str]) -> int:
        count = 0
        
        for i in range(len(strs[0])):
            for j in range(len(strs)):
                if i < len(strs[0]):
                    tmp = strs[j][i]
                    if (j+1 < len(strs)) and ord(strs[j+1][i]) < ord(tmp):
                        count+=1
                        break
        return count
                    