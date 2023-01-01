class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        dict_ = {}
        for i in range(len(nums)):
            complement = target - nums[i]
            if complement in dict_:
                answer = [i,dict_[complement]]
                return answer
            else:
                dict_[nums[i]] = i
        