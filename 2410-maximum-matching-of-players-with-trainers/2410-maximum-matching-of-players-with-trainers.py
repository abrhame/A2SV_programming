class Solution:
    def matchPlayersAndTrainers(self, players: List[int], trainers: List[int]) -> int:
        # first sort both the arrays
        # we can use a two pointer approach to iterate on both the arrays
        players.sort()
        trainers.sort()
        
        n = len(players)
        m = len(trainers)
        
        i = 0
        j = 0
        match = 0
        while i < n and j < m:
            if players[i] <= trainers[j]:
                match += 1
                i += 1
                j += 1
            else:
                j+= 1
        return match
                
                