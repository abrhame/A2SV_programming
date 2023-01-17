class Solution:
    def validMountainArray(self, arr: List[int]) -> bool:
        # if the length of the array is less than 3 it is not a valid Mountain array
        if len(arr) < 3:
            return False
        
        # intialize a flag variable to follow the mountain start to stricly decresing
        flag = False
        idx = 0
        for i in range(len(arr)-1):
            if arr[i] == arr[i+1]: 
                return False
            elif arr[i] > arr[i +1]:
                flag = True # if the array start to decrease intialize the flag to True
                idx = i+1   # index of the array that it starts to decreas strictly
                break
            elif i+1 == (len(arr) - 1):     # check for all arrays are not strictly increasing
                return False
        if flag == True:    # if the flag  is true, check for strictly decreasing
            for i in range(idx,len(arr)-1):
                if arr[i] <= arr[i + 1]:
                    return False
                elif idx == 1 and i+1 == (len(arr) - 1):      # check for all arrays are not strictly decreasing
                    return False
        return True
                
        