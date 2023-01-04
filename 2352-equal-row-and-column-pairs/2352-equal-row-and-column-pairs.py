class Solution:
    def equalPairs(self, grid: List[List[int]]) -> int:
        transpose = list(zip(*grid))
        count = 0
        for i in range(len(grid)):
            for j in range(len(transpose)):
                if grid[i] == list(transpose[j]):
                    count +=1
        return count