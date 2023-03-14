class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        ans = set()

        def backtrack(idx,subsets):
            if tuple(subsets) not in ans:
                ans.add(tuple(subsets[:]))
                
            if idx >= len(nums):
                return
            for i in range(idx,len(nums)):
                subsets.append(nums[i])
                backtrack(i + 1,subsets)
                subsets.pop()
        backtrack(0,[])
        return sorted(ans)