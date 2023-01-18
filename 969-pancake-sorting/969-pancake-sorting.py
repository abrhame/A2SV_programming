class Solution:
    def pancakeSort(self, A: List[int]) -> List[int]:
        """ sort like bubble-sort
            sink the largest number to the bottom at each round
        """
        # our output is going to be the index of flip performed
        ans = []
        
        # a function that performs flips in place
        def flip(arr,k):
            ans.append(k+1)   # the index of the flip going to be performed
            i = 0
            while i < k:
                arr[i], arr[k] = arr[k], arr[i]
                i += 1
                k -= 1
                
        count = 0
        for i in range(len(A)-1,-1,-1):
            max_ = A.index(max(A[0:i+1]))
            # check wether the given list is sorted ans also check for the maximum element is in its expected place. if its in the correct place don't perform the flips
            if max_ == i:
                continue
            flip(A,max_)    # flip the largest element to the 0 index
            flip(A,i)   # flip the largest elemt to the correct postion. i.e next to the previous largest element
            
        # if the number of the count is the same as length of the list then it is already sorted
        return ans
            
            