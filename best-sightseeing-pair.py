class Solution:
    def maxScoreSightseeingPair(self, values: List[int]) -> int:
        maxScore = 0
        maxLeft = values[0]
        for j in range(1, len(values)):
            maxScore = max(maxScore, maxLeft + values[j] - j)
            maxLeft = max(maxLeft, values[j] + j)
        return maxScore