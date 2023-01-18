class Solution:
    def pancakeSort(self, A: List[int]) -> List[int]:
        """ sort like bubble-sort
            sink the largest number to the bottom at each round
        """
        ans = []
        def flip(arr,k):
            ans.append(k+1)
            i = 0
            while i < k:
                arr[i], arr[k] = arr[k], arr[i]
                i += 1
                k -= 1
                
        count = 0
        for i in range(len(A)-1,-1,-1):
            max_ = A.index(max(A[0:i+1]))
            if max_ == i:
                count += 1
                continue
            flip(A,max_)
           
            flip(A,i)
        if count == len(A):
            return []
        else:
            return ans
            
            