class Solution:
    def numJewelsInStones(self, jewels: str, stones: str) -> int:
        lookup = set()
        total_jewels = 0
        for jewel in jewels:
            lookup.add(jewel)
        
        for stone in stones:
            if stone in lookup:
                total_jewels +=1
        return total_jewels