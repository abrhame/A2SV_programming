class Solution:
    def numSubarraysWithSum(self, nums: List[int], goal: int) -> int:
        count = 0
        current_sum = 0
        prefix_sum = {0: 1}

        for num in nums:
            current_sum += num
            count += prefix_sum.get(current_sum - goal, 0)
            prefix_sum[current_sum] = prefix_sum.get(current_sum, 0) + 1

        return count