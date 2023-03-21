class TopVotedCandidate:

    def __init__(self, persons: List[int], times: List[int]):
        self.times = times
        self.leader = []
        votes = Counter()
        winner = -1

        for p in persons:
            votes[p] += 1
            if votes[p] >= votes[winner]:
                winner = p
            self.leader.append(winner)
    def q(self, t: int) -> int:
        left, right = 0, len(self.times) 
        
        while left < right:
            mid = (left + right) // 2
            if t < self.times[mid]:
                right = mid 
            else:
                left = mid + 1
        return self.leader[left - 1]


# Your TopVotedCandidate object will be instantiated and called as such:
# obj = TopVotedCandidate(persons, times)
# param_1 = obj.q(t)