class Solution:
    def shipWithinDays(self, weights: List[int], days: int) -> int:
        left,right = max(weights), sum(weights)
        res = right

        def canShip(cap):
            ships, currCap = 1, cap

            for w in weights:
                if currCap - w < 0:
                    ships += 1
                    currCap = cap
                currCap -= w
            return ships <= days

        while left <= right:
            capacity = (left + right) // 2
            if canShip(capacity):
                res = min(res,capacity)
                right = capacity - 1
            else:
                left = capacity + 1
        return res