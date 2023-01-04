class Solution:
    def equalPairs(self, grid: List[List[int]]) -> int:
        # transpose = list(zip(*grid))
        # count = 0
        # for i in range(len(grid)):
        #     for j in range(len(transpose)):
        #         if grid[i] == list(transpose[j]):
        #             count +=1
        # return count
        trans = []
        for i in range(len(grid)):
            tmp = []
            for j in range(len(grid)):
                tmp.append(grid[j][i])
            trans.append(tmp)
        count = 0
        for i in range(len(grid)):
            for j in range(len(trans)):
                if grid[i] == trans[j]:
                    count +=1
        return count