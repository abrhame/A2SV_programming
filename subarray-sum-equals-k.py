class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        res = 0
        curSum = 0
        prefixSums = Counter([0])
        
        for n in nums:
            curSum += n
            diff = curSum - k
            
            res += prefixSums.get(diff,0)
            prefixSums[curSum] += 1 
        return res