class Solution:
    def find132pattern(self, nums: List[int]) -> bool:
        stack = []
        right = -float('inf')
        for i,num in enumerate(nums[::-1]):
            if num < right:
                return True
            else:
                while stack and stack[-1] < num:
                    right = stack.pop()
            stack.append(num)
        return False