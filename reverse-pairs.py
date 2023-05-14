class Solution:
    def reversePairs(self, nums: List[int]) -> int:
        self.count = 0
        
        def mergeSort(nums):
            if len(nums) <= 1:
                return nums
            mid = len(nums) // 2
            left = mergeSort(nums[:mid])
            right = mergeSort(nums[mid:])
            return merge(left, right)
        
        def merge(left, right):
            i = j = 0
            while i < len(left) and j < len(right):
                if left[i] > 2*right[j]:
                    self.count += len(left) - i
                    j += 1
                else:
                    i += 1
            return sorted(left + right)
        
        mergeSort(nums)
        return self.count