class Solution:        
    def findKthLargest(self, nums: List[int], k: int) -> int:
        def partition(nums,low,high):
            pivot = nums[high]
            i = low - 1
            
            for j in range(low,high):
                if nums[j] <= pivot:
                    i += 1
                    nums[i],nums[j] = nums[j],nums[i]
            nums[i+1],nums[high] = nums[high], nums[i+1]
            return i + 1

        def quick_sort(nums,low,high):
            if low < high:
                pivot = partition(nums,low,high)
                quick_sort(nums,low,pivot - 1)
                quick_sort(nums,pivot + 1, high)
        quick_sort(nums,0, len(nums) - 1)

        return nums[len(nums) - k]