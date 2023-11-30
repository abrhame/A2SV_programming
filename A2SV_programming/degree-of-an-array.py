class Solution:
    def findShortestSubArray(self, nums: List[int]) -> int:
        first = {}
        last = {}
        freq = Counter()

        for i, num in enumerate(nums):
            if num not in first:
                first[num] = i
            last[num] = i
            freq[num] += 1
        
        max_freq = max(freq.values())

        min_len = float('inf')

        for k,v in freq.items():
            if v == max_freq:
                min_len = min(min_len, last[k] - first[k])
        
        return min_len + 1


        