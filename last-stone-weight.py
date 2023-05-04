class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        stones = [-stone for stone in stones]
        heapq.heapify(stones)
        while len(stones) > 1:
            m1 = -heapq.heappop(stones)
            m2 = -heapq.heappop(stones)
            if m1 != m2:
                heappush(stones,-(m1-m2))
        return -stones[0] if len(stones) == 1 else 0