class Solution:
    def sortPeople(self, names: List[str], heights: List[int]) -> List[str]:
        # swap = False
        # for i in range(0,len(names)):
        #     for j in range(len(names) - i - 1):
        #         if heights[j] < heights[j+1]:
        #             swap = True
        #             heights[j],heights[j+1] = heights[j+1],heights[j]
        #             names[j], names[j+1] = names[j+1], names[j]
        #     if swap == False:
        #         return names
        # return names
        
        for i in range(len(names)):
            for j in range(i,len(names)):
                if heights[i] <= heights[j]:
                    heights[i],heights[j] = heights[j],heights[i]
                    names[i], names[j] = names[j], names[i]
        return names
                    
        