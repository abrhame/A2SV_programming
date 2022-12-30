class Solution:
    def sumEvenAfterQueries(self, nums: List[int], queries: List[List[int]]) -> List[int]:
        evensum = 0
        for num in nums:
            if num % 2 == 0:
                evensum += num
        ans = []
        
        for val, idx in queries:
            if nums[idx] % 2 == 0:
                evensum -= nums[idx]
            nums[idx] += val
            
            if nums[idx] % 2 == 0:
                evensum += nums[idx]
            
            ans.append(evensum)
        return ans
            
        