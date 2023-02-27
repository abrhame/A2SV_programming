class Solution:
    def timeRequiredToBuy(self, tickets: List[int], k: int) -> int:
        n = len(tickets)
        l = 0
        time = 0
        c_0 = 0
        while tickets[k] != 0:
            if tickets[l] != 0:
                tickets[l] -= 1
                time += 1
                c_0 = tickets.count(0)
            l += 1
            l %= n
        return time