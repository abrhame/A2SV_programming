class Solution:
    def checkIfExist(self, arr: List[int]) -> bool:
        # given list called arr
        # index i and j
        # i!=j
        # i >= 0
        # j < len(arr)
        # arr[i] == 2 * arr[j]
        # we use two pointer
        # to fulfill the first condition use while loop with no equal assignement
        # intialize the two index according to the seconde rule
        # if the third rule satisfied return true else false
        
        # i = 0
        # j = len(arr) - 1
        # flag = ""
        # arr.sort(reverse = True)
        # while i < j:
        #     if arr[i] == 2*arr[j]:
        #         return True
        #     else:
        #         j-=1
        #         flag = False
        # return flag
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
         
