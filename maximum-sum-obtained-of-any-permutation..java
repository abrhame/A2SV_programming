class Solution:
    def maxSumRangeQuery(self, nums: List[int], requests: List[List[int]]) -> int:
        n = len(nums)
        cnt = [0 for _ in range(n + 1)]
        for i, j in requests:
            cnt[i] += 1
            cnt[j + 1] -= 1
        
        for i in range(1, n + 1):
            cnt[i] += cnt[i - 1]
        
        res = 0
        for v, c in zip(sorted(cnt[:-1]), sorted(nums)):
            res += v * c
        
        return res % (10 ** 9 + 7)