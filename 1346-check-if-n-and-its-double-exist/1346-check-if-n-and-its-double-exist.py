class Solution:
    def checkIfExist(self, arr: List[int]) -> bool:
        count = 0
        for num in arr:
                if num == 0:
                    count += 1
                    continue
                if 2*num in arr:
                     return True
                else:
                     continue
        if count > 1:
            return True
        return False         
         
