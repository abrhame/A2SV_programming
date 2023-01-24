class Solution:
    def maxArea(self, height: List[int]) -> int:
        left = 0
        right = len(height) - 1
        max_am = 0
        
        while left < right:
            # find the diffrence between the two and multiply the diffrenec with smallest ot with the largest and find the maximum
            diff = right - left 
            if height[left] < height[right]:
                max_am = max(diff*height[left], max_am)
                left += 1
            else:
                max_am = max(diff*height[right], max_am)
                right -= 1
        return max_am
            
