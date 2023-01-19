class Solution:
    def replaceElements(self, arr: List[int]) -> List[int]:
        #iterate all over the elment and find the maximum value to the right of the current element and replace it with the maximum value
        max_= 0
        for i in range(len(arr)-1):
            if max_ > 0 and ind > i:
                arr[i] = max_
            else:
                max_= max(arr[i+1:len(arr)])
                ind = arr.index(max_)
                arr[i] = max_
        # make the last element -1
        arr.pop()
        arr.append(-1)
        return arr

        

        