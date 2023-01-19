class Solution:
    def countDistinctIntegers(self, nums: List[int]) -> int:
        rd_arr = []
        
        for num in nums:
            rev_digit = 0
            while num > 0:
                reminder = num % 10
                rev_digit = (rev_digit * 10) + reminder
                num = num // 10
            rd_arr.append(rev_digit)
        nums.extend(rd_arr)
        
        count = Counter(nums)
        return len(count)
        # for i in range(len(nums)):
        #     if nums[i] not in nums[i+1:]:
        #         count +=1
        # for num in rd_arr:
        #     if num not in nums:
        #         count += 1
        # return count
        