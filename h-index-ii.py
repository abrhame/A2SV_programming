class Solution:
    def hIndex(self, citations: List[int]) -> int:

        l, r = 0, len(citations) - 1
        while l <= r:
            mid = (r + l) // 2
            if citations[mid] == len(citations) - mid:
                return len(citations) - mid
            elif citations[mid] < len(citations) - mid:
                l = mid + 1
            else:
                r = mid - 1
                
        return len(citations) - l