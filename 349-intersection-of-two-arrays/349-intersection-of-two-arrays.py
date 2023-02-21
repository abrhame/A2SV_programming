class Solution:
    def intersection(self, nums1: List[int], nums2: List[int]) -> List[int]:
        nums1.sort()
        nums2.sort()
        ans = set()
        p = 0
        for num in nums1:
            if num in nums2[p:]:
                ans.add(num)
                p = nums2.index(num) + 1
        return list(ans)
        
        