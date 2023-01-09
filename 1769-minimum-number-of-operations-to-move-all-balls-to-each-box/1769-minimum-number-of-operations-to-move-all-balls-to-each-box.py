class Solution:
    def minOperations(self, boxes: str) -> List[int]:
        
        ans = []
        
        for i in range(len(boxes)):
            step = 0
            for j in range(len(boxes)):
                if boxes[j] == "1":
                    step += abs(j - i)
            ans.append(step)
            
        return ans