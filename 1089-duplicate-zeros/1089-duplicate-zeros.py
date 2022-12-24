class Solution:
    def duplicateZeros(self, arr: List[int]) -> None:
        """
        Do not return anything, modify arr in-place instead.
        """
        #iterate over the array and if you found 0 inser 0 next to it index at the same time remove one element at the end
        i = 0
        while i <len(arr):
            if arr[i] == 0:
                arr.insert(i+1, 0)
                i=i+2
                arr.pop()
            else:
                i +=1
        