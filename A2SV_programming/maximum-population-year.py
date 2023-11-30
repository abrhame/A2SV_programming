class Solution:
    def maximumPopulation(self, logs: List[List[int]]) -> int:
        log = [0] * 101
        for i in range(len(logs)):
            log[logs[i][0] - 1950] += 1
            log[logs[i][1] - 1950] -= 1

        prefix = list(accumulate(log))

 
        return prefix.index(max(prefix)) + 1950
        