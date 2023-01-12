        p = 0
        for i in range(len(nums)):
            if nums[i] != 0:
                nums[p] = nums[i]
                p = p+1
        for i in range(p,len(nums)):
            nums[i] = 0
        return nums
